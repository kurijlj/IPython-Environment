from os import listdir
from os.path import isdir, exists


def ls(path):
    for file in listdir(path):
        print(file)


class OsDirectory(object):
    """Wrapper for common os module directory functions.

    Attributes:
        _path (str): string representing path to directory. If not provided on
                     instantiation '.' is used as default value.
    """

    def __init__(self, path: str='.'):
        """Initialize self.

        Arguments:
            path (str): string to be assigned to the _path attribute. Default
                        value is '.'.
        """

        if type(path) is not str:
            raise ValueError('Parameter \'{0}\' is not a string'.format(path))
            self._path = '.'
        else:
            self._path = path

    def __repr__(self):
        """Return 'path' string.
        """

        return '\'{0}\''.format(self._path)

    def __str__(self):
        """Return 'path' string.
        """

        return self._path

    def exists(self):
        """Wrapper for os.path.exists().

        Returns:
            bool: True if '_path' refers to an existing file/directory. If
                  'path' refers to a broken symbolick link, or permission is
                  not granted to execute os.stat() (platform dependant) on the
                  file/directory that 'path' refers to, or simply 'path' refers
                  to non-existing file/directory then it is False.
        """

        return exists(self._path)

    def isdir(self):
        """Wrappper for os.path.isdir().

        Note:
            It follows symbolic links.

        Returns:
            bool: True if '_path' refers to an existing directory,
                  False otherwise.
        """

        return isdir(self._path)

    def list(self):
        """Wrapper for os.listdir().

        Print entries for given directory path.

        Raises:
            OSError: If 'path' refers to non-existing, or
                     not accessible directory.
            NotADirectoryError: If 'path' refers to a file.
        """

        if not self.exists():
            pass
            raise OSError('\'{0}\''.format(self._path))
        elif not self.isdir():
            raise NotADirectoryError('\'{0}\''.format(self._path))
        else:
            for file in listdir(self._path):
                print(file)


class IsTrue(object):
    """Class for evaluating truth value of an object.

    By default, an object is considered True unless its class defines either
    a __bool__() method that returns False or a __len__() method that returns
    zero, when called with the object. Here are most of the built-in objects
    considered false:
        - constants defined to be false: None and False.
        - zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
        - empty sequences and collections: '', (), [], {}, set(), range(0)

    Attributes:
        _obj (object): object to be avaluated for truth value. If not provided
                       on instantiation None is used as default value.
    """

    def __init__(self, obj=None):
        """Initialize self.

        Arguments:
            obj (object): object to be assigned to the _obj attribute. Default
                          value is None.
        """

        self._obj = obj

    def __repr__(self):
        """Return str(self._obj)
        """

        return str(self._obj)

    def __str__(self):
        """Return str(self._obj).
        """

        return str(self._obj)

    def type(self):
        """Return type of an object stored in _obj attribute.

        Returns:
            type class: type(self._obj).
        """

        return type(self._obj)

    def evaluate(self):
        """Return result of object truth value testing.

        Returns:
            bool: True if _obj evaluates to True, False otherwise.
        """

        if self._obj:
            return True
        else:
            return False
