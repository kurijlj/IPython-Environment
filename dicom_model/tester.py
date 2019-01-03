#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tester.py

from dicomdatastructures import SliceLocation
from dicom.valuerep import DSdecimal, DSfloat

def main():
    # SliceLocation tests
    a = SliceLocation(101)
    b = SliceLocation(57)
    c = SliceLocation(101)
    
    try:
        d = SliceLocation(101.0)
    except Exception as e:
        print (e)

    try:
        e = SliceLocation('101')
    except Exception as e:
        print(e)

    print(a, '\n', b, '\n', c, '\n', d, '\n', e)
    print('a == b: ', a == b)
    print('a == c: ', a == c)
    print('a == d: ', a == d)
    print('a == e: ', a == e)
    print('d == e: ', d == e)
    print('a != b: ', a != b)
    print('a != c: ', a != c)
    print('a != d: ', a != d)
    print('a != e: ', a != e)
    print('d != e: ', d != e)

    print(a.value, '[', type(a.value), ']\n')
    print(b.value, '[', type(b.value), ']\n')
    print(c.value, '[', type(c.value), ']\n')
    print(d.value, '[', type(d.value), ']\n')
    print(e.value, '[', type(e.value), ']\n')


if __name__ == '__main__':
    main()
