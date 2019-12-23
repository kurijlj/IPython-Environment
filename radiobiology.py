#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
from sys import stderr
# from collections import namedtuple


# DVHPoint = namedtuple('DVHPoint', ['dose', 'volume'])


def cdvh_from_file(fn, delimiter):
    """ Load cDVH data form CSV file. It is up to user to ensure that given file
        contains cumulative DVH data.
    """

    # Let first count the number of data points, keeping in mind that first row
    # is reserved for columns headers.
    for n, l in enumerate(fn):
        pass

    cdvh = np.zeros((n, 2))

    # Set file pointer to the beginning of a file
    fn.seek(0, 0)

    for n, line in enumerate(fn):
        if 0 < n:
            #print(line.rstrip().split(sep=delimiter))
            values = line.rstrip().split(sep=delimiter)
            cdvh[n-1, 0] = float(values[0])
            cdvh[n-1, 1] = float(values[1])

            if 0 > cdvh[n-1, 0] or 0 > cdvh[n-1, 1]:
                print(
                    "DVH data in file \'{0}\' contain negative value(s) in line: {1}"
                    .format(fn.name, n+1),
                    file=stderr
                    )
                return None

    return cdvh


def RE(dstd: float, ab: float):
    """ Calculate relative effectivnes (RE) as:
            RE = (1 + dstd/ab)
        where dstd is dose per fraction for standard fractination
        (1.8 Gy <= X <= 2.5 Gy) and ab is a tissue alpha/beta ratio.
    """

    if dstd < 1.8 and dstd > 2.5:
        raise ValueError(
            "Not a standard daily fraction value: {0} Gy".format(dstd)
            )

    return (1.0 + dstd/ab)


def BED(d: float, fr: int, ab: float):
    """ Calculate biologically effective dose (BED) as:
            BED = D * (1.0 + (d/ab))
        where d is dose per fraction, fr is number of fractions and ab is a
        tissue alpha/beta ratio.
    """
    return (d*fr)*(1.0+(d/ab))


def EQDXab(d: float, fr: int, dstd: float, ab: float):
    """ Calculate biologically equivalent total dose in standard daily fractions
         as:
            EQDXab = BED / RE
    """

    return BED(d, fr, ab) / RE(dstd, ab)
