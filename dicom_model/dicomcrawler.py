#!/usr/bin/env python
# -*- coding: utf-8 -*-
# dicomcrawler.py

from __future__ import print_function
import os
import argparse
import sys
# import fnmatch
from pprint import pformat
import pydicom
import dicomdatastructures as dcds


def find_dicom_files(directory, recursive=True):
    """Search a root directory for all files matching a given pattern (in
    Glob format - *.dcm etc) and that have the "DICM" magic number returns
    a full path name.
    """
    for root, dirs, files in os.walk(directory):
        if not recursive:
            dirs = []
        for basename in files:
            filename = os.path.join(root, basename)
            with open(filename, 'rb') as f:
                x = f.read(132)
            if x[128:] == b'DICM':
                yield filename


def parse_args(argv=None):
    """Argument parser for Dicom Tools
    """
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser(
        description='Scan a directory of dicom files '
                    'and assemble a list of patient, '
                    'study, series, image sets')
    parser.add_argument('-d', '--dicom-dir',
                        dest='dicom_dir',
                        type=str,
                        help='Directory of dicom files ',
                        default='.')
    parser.add_argument('-r', '--recursive',
                        dest='recursive',
                        action='store_true',
                        help='Process recursively')
    parser.add_argument('--no-recursive',
                        dest='recursive',
                        action='store_false',
                        help='Do not process recursively')
    parser.set_defaults(recursive=True)
    return parser.parse_args()


def main(argv=None):
    """main for dicom_dir
    """
    if argv is None:
        argv = sys.argv
    args = parse_args(argv=argv[1:])
    print(pformat(args))
    patients = list()
    for x in find_dicom_files(directory=args.dicom_dir,
                              recursive=args.recursive):
        f = dcds.DicomDatasetAdapter(pydicom.dcmread(x))
        for p in patients:
            try:
                p.add_dataset(f)
            except Exception:
                pass
            else:
                break
        else:
            patients.append(dcds.Patient(dicom_dataset=f))
    print('Found', len(patients), 'patients')
    for x in patients:
        print('\n')
        print(repr(x))


if __name__ == '__main__':
    main()
