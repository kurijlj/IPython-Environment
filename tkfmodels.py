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

class User(object):
    """ A demo class representing user with general data about user.
    """

    def __init__(self, un='user', psswd='p4s5w0rd', fn=None, ln=None):
        self._username = un
        self._password = psswd
        self._firstname = fn
        self._lastname = ln

    def __repr__(self):
        str_type = type(self).__name__
        str_un = 'Username: {0}'.format(self._username)
        str_psswd = 'Password: {0}'.format(self._password)

        if self._firstname:
            str_fn = 'First Name: {0}'.format(self._firstname)
        else:
            str_fn = 'First Name: N/A'

        if self._lastname:
            str_ln = 'Last Name: {0}'.format(self._lastname)
        else:
            str_ln = 'Last Name: N/A'

        return str_type + '(\n' + str_un + ',\n' + str_psswd + ',\n' +\
            str_fn + ',\n' + str_ln + '\n)'

    def changepassword(self, pw):
        checktype(str, pw, 'Password')
        self._password = pw

    def changefirstname(self, fn):
        checktype(str, fn, 'First name')
        self._firstname = fn

    def changelastname(self, ln):
        checktype(str, ln, 'Last name')
        self._lastname = ln

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def firstname(self):
        return self._firstname

    @property
    def lastname(self):
        return self._lastname


class QAFilm(object):
    """ An abstract base class used to represent scanned dosimetric film image
    and a set of common methods to access and manipulate film data.
    """

    def __init__(self, imagedata, controller):
        # It is up to user to ensure that proper image data is passed.
        self._imagedata = imagedata
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
        # By calling rotate method we are not doing actual rotation of an
        # image, we are just recording the angle by wich to rotate a copy of
        # the image when accessing image pixels using pixels_from_selection()
        # method. This is done for better image preview after rotation, because
        # we set flag "expand" to "True" on rotate() method call. Subsequent
        # image rotations are recorded as an array and final image rotation is
        # calculated as sum of all subsequent image rotations.
        self._imagerotation = np.append(self._imagerotation, angle)

    def undo_rotation(self):
        # Removes last rotation (last element of the array). If only initial
        # angle of rotation is left (0.0) disregard request.
        if 1 < self._imagerotation.size:
            self._imagerotation = np.delete(self._imagerotation, -1)

    def pixels_from_selection(self, bounds):
        # Method to return selection from image as numpy array. Selection
        # extents are defined by "bounds" variable which is of type
        # SelectionExtents. Variable "colormode" is used to specify which data
        # of a selection to retrieve: fullcolor, grayscale, red channel, green
        # channel or blue channel. Default value is fullcolor.

        pixels = None
        selection = None

        # First roatate image according to rotation history data array.
        img_rt = self._imagedata.rotate(
                angle=-self._imagerotation.sum(),  # negative sign to rotate
                                                   # clockwise
                resample=Image.NEAREST,
                expand=True,
                fillcolor='white'
            )

        if ImageColorMode.grayscale == self._colormode:
            pixels = np.asarray(img_rt.convert('L'))
        elif ImageColorMode.red == self._colormode:
            pixels = np.asarray(img_rt.getchannel('R'))
        elif ImageColorMode.green == self._colormode:
            pixels = np.asarray(img_rt.getchannel('G'))
        elif ImageColorMode.blue == self._colormode:
            pixels = np.asarray(img_rt.getchannel('B'))
        else:
            pixels = np.asarray(img_rt)

        selection = pixels[
                bounds.top:bounds.bottom+1,
                bounds.left:bounds.right+1
            ]

        return selection

    @property
    def image_dpi(self):
        # Read value of an image dpi.
        result = None
        if 'dpi' in self._imagedata.info:
            result = self._imagedata.info['dpi']
        return result

    @property
    def colormode(self):
        return self._colormode

    @property
    def size(self):
        # Returns image size in pixels as SelectionExtents object. This relates
        # to original image, without applied transformations.
        result = SelectionExtents(
                top=int(0),
                left=int(0),
                bottom=self._imagedata.height,
                right=self._imagedata.width
            )
        return result

    @property
    def width(self):
        # Returns image width in pixels. This relates to original image,
        # without applied transformations.
        return self._imagedata.width

    @property
    def height(self):
        # Returns image width in pixels. This relates to original image,
        # without applied transformations.
        return self._imagedata.height
