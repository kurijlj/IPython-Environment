#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tester.py

from dds import SliceLocation
try:
    from pydicom.valuerep import DSdecimal, DSfloat
except ImportError:
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
    h = SliceLocation(None)

    print('a = {0};'.format(a))
    print('is a an \'None\'? {0}', a.is_none())
    print('is a an empty string? {0}', a.is_empty_string())
    print('is a an \'DSclass\'? {0}', a.is_dsclass())

    print('b = {0};'.format(b))
    print('is b an \'None\'? {0}', b.is_none())
    print('is b an empty string? {0}', b.is_empty_string())
    print('is b an \'DSclass\'? {0}', b.is_dsclass())

    print('c = {0};'.format(c))
    print('is c an \'None\'? {0}', c.is_none())
    print('is c an empty string? {0}', c.is_empty_string())
    print('is c an \'DSclass\'? {0}', c.is_dsclass())

    print('d = {0};'.format(d))
    print('is d an \'None\'? {0}', d.is_none())
    print('is d an empty string? {0}', d.is_empty_string())
    print('is d an \'DSclass\'? {0}', d.is_dsclass())

    print('e = {0};'.format(e))
    print('is e an \'None\'? {0}', e.is_none())
    print('is e an empty string? {0}', e.is_empty_string())
    print('is e an \'DSclass\'? {0}', e.is_dsclass())

    print('f = {0};'.format(f))
    print('is f an \'None\'? {0}', f.is_none())
    print('is f an empty string? {0}', f.is_empty_string())
    print('is f an \'DSclass\'? {0}', f.is_dsclass())

    print('g = {0};'.format(g))
    print('is g an \'None\'? {0}', g.is_none())
    print('is g an empty string? {0}', g.is_empty_string())
    print('is g an \'DSclass\'? {0}', g.is_dsclass())

    print('h = {0};'.format(h))
    print('is h an \'None\'? {0}', h.is_none())
    print('is h an empty string? {0}', h.is_empty_string())
    print('is h an \'DSclass\'? {0}', h.is_dsclass())

    print('a == a: ', a == a)
    print('a == b: ', a == b)
    print('a == c: ', a == c)
    print('a == d: ', a == d)
    print('a == e: ', a == e)
    print('a == f: ', a == f)
    print('a == g: ', a == g)
    print('a == h: ', a == h)
    print('a != a: ', a != a)
    print('a != b: ', a != b)
    print('a != c: ', a != c)
    print('a != d: ', a != d)
    print('a != e: ', a != e)
    print('a != f: ', a != f)
    print('a != g: ', a != g)
    print('a != h: ', a != h)

    print(a.value, '[', type(a.value), ']')
    print(b.value, '[', type(b.value), ']')
    print(c.value, '[', type(c.value), ']')
    print(d.value, '[', type(d.value), ']')
    print(e.value, '[', type(e.value), ']')
    print(f.value, '[', type(f.value), ']')
    print(g.value, '[', type(g.value), ']')
    print(h.value, '[', type(h.value), ']')


if __name__ == '__main__':
    main()
