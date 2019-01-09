#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tester.py

from dds import SliceLocation
from dicom.valuerep import DSdecimal, DSfloat

def main():
    # SliceLocation tests
    a = SliceLocation(DSdecimal('133.45'))
    b = SliceLocation(DSdecimal('133.45'))
    c = SliceLocation(DSdecimal('13.45'))
    d = SliceLocation(DSfloat('133.45'))
    e = SliceLocation(DSfloat('33.45'))
    f = SliceLocation(DSdecimal(''))
    g = SliceLocation('')
    h = None
    try:
        h = SliceLocation(None)
    except Exception as e:
        print (e)
    
    print(a, '\n', b, '\n', c, '\n', d, '\n', e, '\n', f, '\n', g, '\n', h)
    print('a == a: ', a == a)
    print('a == b: ', a == b)
    print('a == c: ', a == c)
    print('a == d: ', a == d)
    print('a == e: ', a == e)
    print('a == f: ', a == f)
    print('a == g: ', a == g)
    print('a == h: ', a == h)
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
