#!/usr/bin/env python3
# =============================================================================
# <one line to give the program's name and a brief idea of what it does.>
#
#  Copyright (C) <yyyy> <Author Name> <author@mail.com>
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option)
# any later version.
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
#
# =============================================================================


# =============================================================================
#
# <Put documentation here>
#
# <yyyy>-<mm>-<dd> <Author Name> <author@mail.com>
#
# * <programfilename>.py: created.
#
# =============================================================================


# =============================================================================
#
# TODO:
#
# * Add check if selection is within image limits for methods
#   pixels_from_selection(), inline_profile(), and crossline_profile(). Throw
#   an exception in the case they are not.
#
# =============================================================================

import numpy as np
from PIL import Image  # Required by image rotation in the QAFilm class
from tkfutils import (
        SelectionExtents,
        ImageColorMode,
        checktype
    )
from skimage.feature import canny  # Required for edge detection
from skimage.filters import threshold_otsu

# =============================================================================
# Models specific utility classes and functions
# =============================================================================


# =============================================================================
# Model classes
# =============================================================================

class QAFilm(object):
    """ An abstract base class used to represent scanned dosimetric film image
    and a set of common methods to access and manipulate film data.
    """

    def __init__(self, imagedata, controller):

        # It is up to user to ensure that proper image data is passed.

        # List contining original image and rotated copies of
        # the original image.
        self._imagedata = [imagedata]
        self._controller = controller
        # Parameter used to track display color mode of the image.
        self._colormode = ImageColorMode.fullcolor
        # Array used to accumulate subsequent rotations of the image.
        self._imagerotation = np.array([0.0], np.single)

    def change_color_mode(self, colormode):
        # Set display color mode of the image. Parameter colormode must be of
        # the type ImageColorMode.
        checktype(ImageColorMode, colormode, 'Colormode')
        self._colormode = colormode

    def rotate(self, angle):
        # Since we are using following options when doing image rotation:
        # resample=Image.NEAREST and expand=True, for better image privew we
        # are actually accumulating all subsequent rotations of an image in the
        # container of type np.array.and then apply cumulative rotation value
        # to the original image.

        # First discard previously rotated image.
        if 1 < len(self._imagerotation):
            self._imagedata.pop()

        self._imagerotation = np.append(self._imagerotation, angle)

        # Calculate cumulative rotation angle regarding to original
        # image position, and apply this value for obtaining the latest image
        # preview.
        rotation_angle = self._imagerotation.sum()
        self._imagedata.append(self._imagedata[-1].rotate(
                angle=-rotation_angle,  # negative sign to rotate clockwise
                resample=Image.NEAREST,
                expand=True,
                fillcolor='white'
            ))

    def detect_edges(self, sigma, lowtr, hightr):

        # First we do a dummy image rotation just to be able to undo. This
        # should be removed in the release version.
        self._imagerotation = np.append(self._imagerotation, 0.0)

        # data = 255 - np.asarray(self._imagedata[-1].getchannel('R'))
        # edges = canny(
        #         data,
        #         sigma=sigma,
        #         low_threshold=lowtr,
        #         high_threshold=hightr
        #     )
        self._imagedata.append(Image.fromarray(canny(
                np.asarray(self._imagedata[-1].getchannel('R')),
                sigma=sigma,
                low_threshold=lowtr,
                high_threshold=hightr
            )))
        # self._imagedata.append(Image.fromarray(threshold_otsu(
        #         np.asarray(self._imagedata[-1].getchannel('R'))
        #     )))

    def undo_rotation(self):
        # Removes last rotation (last element of the array). If only initial
        # angle of rotation is left (0.0) disregard request.
        if 1 < len(self._imagerotation):

            # First disregard previous rotation value and rotated image.
            self._imagerotation = np.delete(self._imagerotation, -1)
            self._imagedata.pop()

            # Calculate new image preview.
            rotation_angle = self._imagerotation.sum()
            self._imagedata.append(self._imagedata[-1].rotate(
                    angle=-rotation_angle,  # negative sign to rotate clockwise
                    resample=Image.NEAREST,
                    expand=True,
                    fillcolor='white'
                ))

    def ascolormode(self, colormode):
        # Method to extract full size image data of the latest image transform
        # according to the given colormode. If colormode is omitted it returns
        # data according to currently set colormode.

        pixels = None

        if not colormode:
            colormode = self._colormode

        if ImageColorMode.grayscale == colormode:
            pixels = np.asarray(self._imagedata[-1].convert('L'))
        elif ImageColorMode.red == colormode:
            pixels = np.asarray(self._imagedata[-1].getchannel('R'))
        elif ImageColorMode.green == colormode:
            pixels = np.asarray(self._imagedata[-1].getchannel('G'))
        elif ImageColorMode.blue == colormode:
            pixels = np.asarray(self._imagedata[-1].getchannel('B'))
        else:
            pixels = np.asarray(self._imagedata[-1])

        return pixels

    def pixels_from_selection(self, bounds, colormode=None):
        # Method to return selection from image as numpy array. Selection
        # extents are defined by "bounds" variable which is of type
        # SelectionExtents. We don't check if selection extents are within
        # image limits since input for selection extents is based on a image
        # preivew in the image view. Selection is taken from the latest image
        # transformation.
        #
        # Variable "colormode" is used to specify which data
        # of a selection to retrieve: fullcolor, grayscale, red channel, green
        # channel or blue channel. Default value is fullcolor.

        return self.ascolormode(colormode)[
                bounds.top:bounds.bottom+1,
                bounds.left:bounds.right+1
            ]

    def selection_mean(self, bounds, colormode=None):
        # Returns average pixel value for selected region of the image,
        # according to the given colormode. In the case of fullcolor image it
        # returns average pixel value of the image converted to the grayscale.

        if not colormode or ImageColorMode.fullcolor == colormode:
            colormode = ImageColorMode.grayscale

        return self.pixels_from_selection(bounds, colormode).mean()

    def inline_profile(self, column, colormode=None):
        # Method calls pixel_from_selection() method to extract pixel data from
        # the latest image transformation according to color mode. Then profile
        # data is extracted from such pixeldata accordin to column index. We
        # don't check if column index is out of image limits sinc input for the
        # column index is taken from an image preview in the image view.

        return self.ascolormode(colormode)[:, column]

    def inline_profile_mean(self, column, colormode=None):
        # Returns average pixel value for the given image column, according to
        # the given colormode. In the case of fullcolor image it returns
        # average pixel value of the image converted to the grayscale.

        if not colormode or ImageColorMode.fullcolor == colormode:
            colormode = ImageColorMode.grayscale

        return self.inline_profile(column, colormode).mean()

    def crossline_profile(self, row, colormode=None):
        # Method calls pixel_from_selection() method to extract pixel data from
        # the latest image transformation according to color mode. Then profile
        # data is extracted from such pixeldata accordin to row index. We don't
        # check if row index is out of image limits sinc input for the row
        # index is taken from an image preview in the image view.

        return self.ascolormode(colormode)[row, :]

    def crossline_profile_mean(self, row, colormode=None):
        # Returns average pixel value for the given image row, according to
        # the given colormode. In the case of fullcolor image it returns
        # average pixel value of the image converted to the grayscale.

        if not colormode or ImageColorMode.fullcolor == colormode:
            colormode = ImageColorMode.grayscale

        return self.crossline_profile(row, colormode).mean()

    @property
    def image_dpi(self):
        # Read value of an image dpi. We read dpi from original image since it
        # is an metadata and we use it for converting lengths to centimeters.
        result = None
        if 'dpi' in self._imagedata[0].info:
            result = self._imagedata[0].info['dpi']
        return result

    @property
    def colormode(self):
        return self._colormode

    @property
    def size(self):
        # Returns image size in pixels as SelectionExtents object. It relates
        # to size of the transformed image.
        result = SelectionExtents(
                top=int(0),
                left=int(0),
                bottom=self._imagedata[-1].height,
                right=self._imagedata[-1].width
            )
        return result

    @property
    def width(self):
        # Returns image width in pixels. It relates to the width of
        # the transformed image.
        return self._imagedata[-1].width

    @property
    def height(self):
        # Returns image height in pixels. It realtes to the height of
        # the transformed image.
        return self._imagedata[-1].height
