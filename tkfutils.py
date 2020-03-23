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

from enum import Enum  # Required by ImageFromats.
from imghdr import what  # Required by is_mage_format_supported().
from sys import float_info as fi  # Required by MIN_FLOAT and MAX_FLOAT
from collections import namedtuple  # Required by SelectionExtent custom class.


# =============================================================================
# Global constants
# =============================================================================

# Centimeters per inch.
CM_PER_IN = 2.54

MIN_FLOAT = fi.min
MAX_FLOAT = fi.max


# =============================================================================
# General utility classes and functions
# =============================================================================

# Named tuple used to represent selection extents of an film image.
SelectionExtents = namedtuple(
    'SelectionExtents',
    ['top', 'left', 'bottom', 'right']
    )


class ImageFormats(Enum):
    """Class to wrap up enumerated values that define supoported image formats.
    """

    png = 'png'
    tiff = 'tiff'


class ImageColorMode(Enum):
    """An utility class to wrap up possible color modes of an image.
    """

    fullcolor = 'fullcolor'
    grayscale = 'grayscale'
    red = 'R'
    green = 'G'
    blue = 'B'


class Message(Enum):
    """An utility class to enumarate messages that can be exchanged between GUI
    elements via mediator (controller) object.
    """

    cmchngd = 0  # The image color mode has changed.
    imgrt = 1    # Rotate the image.
    unimgrt = 2  # Undo image rotation.


def checktype(tp, var, vardsc):
    """Utility routine used to check if given variable (var) is of requested
    type (tp). If not it raises TypeError exception with a appropriate message.
    Variable description (vardsc) is used for formatting more descriptive error
    messages on rising exception.
    """

    if var is not None and type(var) is not tp:
        raise TypeError('{0} must be {1} or NoneType, not {2}'.format(
            vardsc,
            tp.__name__,
            type(var).__name__
        ))


def is_image_format_supported(filename):
    """Test if file is one of the image formats supported by application.
    Supported image formats are defined by enumerated class ImageFormats.
    """

    image_type = what(filename)

    if image_type:
        try:
            ImageFormats(image_type)
            return True
        except ValueError:
            # We just want to stop exception to propagate further up. Nothing
            # to do here actually, so we just pass.
            pass

    return False


def points_to_centimeters(dpi, this_many_points):
    """Utility function to convert from pixels (points) to centimeters
    according to given dpi (dots per inch).
    """

    # Set deafult return value. Default is negative value that is used to
    # indicate missing or false input values.
    result = -1

    # Do sam basic sanity checks first.
    if 0 < dpi and 0 <= this_many_points:
        result = (this_many_points / dpi) * CM_PER_IN

    return result


def rgb_to_grayscale(red, green, blue):
    """Utility function to calculate grayscale value of an RGB pixel using
    luminosity method: 0.3R + 0.59G + 0.11B.
    """

    return 0.3 * red + 0.59 * green + 0.11 * blue
