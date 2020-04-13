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

import numpy as np
from PIL import Image  # Required by image rotation in the QAFilm class
from tkfutils import (
        SelectionExtents,
        ImageColorMode,
        checktype
    )

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
        # resample=Image.NEAREST and expand=True, for better image privew we are
        # actually accumulating all subsequent rotations of an image in the
        # container of type np.array.and then apply cumulative rotation value to
        # the original image.

        # First discard previously rotated image.
        if 1 < len(self._imagerotation):
            self._imagedata.pop()

        self._imagerotation = np.append(self._imagerotation, angle)

        # Calculate cumulative rotation angle regarding to original
        # image position, and apply this value for obtaining the latest image
        # preview.
        print(rotation_angle)
        self._imagedata.append(self._imagedata[-1].rotate(
                angle=-rotation_angle,  # negative sign to rotate clockwise
                resample=Image.NEAREST,
                expand=True,
                fillcolor='white'
            ))

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

    def pixels_from_selection(self, bounds):
        # Method to return selection from image as numpy array. Selection
        # extents are defined by "bounds" variable which is of type
        # SelectionExtents. Variable "colormode" is used to specify which data
        # of a selection to retrieve: fullcolor, grayscale, red channel, green
        # channel or blue channel. Default value is fullcolor.

        pixels = None
        selection = None

        # First extract full complete image data according to colormode.
        if ImageColorMode.grayscale == self._colormode:
            pixels = np.asarray(self._imagedata[-1].convert('L'))
        elif ImageColorMode.red == self._colormode:
            pixels = np.asarray(self._imagedata[-1].getchannel('R'))
        elif ImageColorMode.green == self._colormode:
            pixels = np.asarray(self._imagedata[-1].getchannel('G'))
        elif ImageColorMode.blue == self._colormode:
            pixels = np.asarray(self._imagedata[-1].getchannel('B'))
        else:
            pixels = np.asarray(self._imagedata[-1])

        # Then extract section according to given bounds.
        selection = pixels[
                bounds.top:bounds.bottom+1,
                bounds.left:bounds.right+1
            ]

        return selection

    @property
    def image_dpi(self):
        # Read value of an image dpi.
        result = None
        if 'dpi' in self._imagedata[-1].info:
            result = self._imagedata[-1].info['dpi']
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
