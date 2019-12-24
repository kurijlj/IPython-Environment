#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
from sys import stderr
# from collections import namedtuple


# DVHPoint = namedtuple('DVHPoint', ['dose', 'volume'])


def total_volume_from_ddvh(dvh):
    """ Calculate total volume from DVH dataset.
    """

    total_volume = 0

    for a in dvh:
        total_volume = total_volume + a[1]

    return total_volume


def normalized_ddvh(ddvh, fr, dstd, ab):
    """ Normalize differential DVH dataset biologically equivalent dose and
        the total volume.
    """

    total_volume = total_volume_from_ddvh(ddvh)
    ndvh = np.zeros(ddvh.shape, dtype=np.double)

    for i, dv in enumerate(ddvh):
        ed = EQDXab(dv[0], fr, dstd, ab)
        nv = dv[1] / total_volume
        ndvh[i, 0] = ed
        ndvh[i, 1] = nv

    return ndvh


def dvh_from_file(fn, delimiter):
    """ Load DVH data form CSV file. It is up to user to track is it a
        cumulative DVH or a differential DVH.
    """

    # Let first count the number of data points, keeping in mind that first row
    # is reserved for columns headers.
    for n, l in enumerate(fn):
        pass

    # Verify that the DVH has at least two rows of data.
    if 2 > n:
        print(
            "ERROR: DVH in the file \'{0}\' has too few rows (minimum required =2)."
            .format(fn.name),
            file=stderr
            )
        return None

    dvh = np.zeros((n, 2), dtype=np.double)

    # Set file pointer to the beginning of a file.
    fn.seek(0, 0)

    for n, line in enumerate(fn):
        if 0 < n:
            #print(line.rstrip().split(sep=delimiter))
            values = line.rstrip().split(sep=delimiter)

            # Verify that the DVH has exactly two columns.
            if 2 != len(values):
                print(
                    "ERROR: DVH in the file \'{0}\' does not have required number of data colums (2)."
                    .format(fn.name),
                    file=stderr
                    )
                return None

            dvh[n-1, 0] = float(values[0])
            dvh[n-1, 1] = float(values[1])

            # Verify that the DVH has no negative values of doses or
            # volumes.
            if 0 > dvh[n-1, 0] or 0 > dvh[n-1, 1]:
                print(
                    "ERROR: DVH data in file \'{0}\' contain negative value(s) in line: {1}"
                    .format(fn.name, n+1),
                    file=stderr
                    )
                return None

    return dvh


def cdvh_to_ddvh(cdvh):
    """ Convert cumulative DVH to diferential DVH.
    """

    ddvh = np.zeros(cdvh.shape, dtype=np.double)

    for i, dv in enumerate(cdvh):
        if 0 < i:
            ddvh[i-1, 0] = cdvh[i-1, 0] + (cdvh[i, 0] - cdvh[i-1, 0]) / 2.0
            if 0 >= (cdvh[i, 0] - ddvh[i-1, 0]):
                print(
                    "ERROR: Dose data error in column 1, rows {0}, {1}."
                    .format(i-1, i),
                    file=stderr
                    )
                return None
            ddvh[i-1, 1] = cdvh[i-1, 1] - cdvh[i, 1]
            if 0 > ddvh[i-1, 1]:
                print(
                    "ERROR: Volume bin < 0 in column 2, rows {0}, {1}."
                    .format(i-1, i),
                    file=stderr
                    )
                print(cdvh[i-1, 1], cdvh[i, 1], ddvh[i-1, 1])
                return None
    ddvh[i, 0] = cdvh[i, 0]

    return ddvh


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


def EUD(nddvh, a):
    """ Calculate EUD from normalized differential DVH dataset.
    """

    eud = 0

    for dv in nddvh:
        eud = eud + dv[1] * pow(dv[0], a)
    eud = pow(eud, 1 / a)

    return eud


def NTCP(eud, td50, gamma50):
    """ Calculate NTCP.
    """

    return 1.0 / (1.0 + pow((td50 / eud), (4.0 * gamma50)))