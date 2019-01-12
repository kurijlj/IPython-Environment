#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tester.py

try:
    from pydicom.valuerep import DSdecimal, DSfloat
except ImportError:
    from dicom.valuerep import DSdecimal, DSfloat
from tabulate import tabulate
from dds import SliceLocation, SliceShape
from colored import fg, attr


def colorize(expression):
    if expression:
        return fg('sandy_brown') + 'True' + attr('reset')

    return 'False'


def slice_location_tests():
    a = SliceLocation(DSdecimal('133.45'))
    b = SliceLocation(DSdecimal('133.45'))
    c = SliceLocation(DSdecimal('13.45'))
    d = SliceLocation(DSfloat('133.45'))
    e = SliceLocation(DSfloat('33.45'))
    f = SliceLocation(DSdecimal(''))
    g = SliceLocation('')
    h = SliceLocation(None)

    objects = [
            ['variable', 'value', 'type', 'is None', 'is empty string',
                'is DSclass'],
            ['a', repr(a), type(a.value), colorize(a.is_none()),
                colorize(a.is_empty_string()), colorize(a.is_dsclass())],
            ['b', repr(b), type(b.value), colorize(b.is_none()),
                colorize(b.is_empty_string()), colorize(b.is_dsclass())],
            ['c', repr(c), type(c.value), colorize(c.is_none()),
                colorize(c.is_empty_string()), colorize(c.is_dsclass())],
            ['d', repr(d), type(d.value), colorize(d.is_none()),
                colorize(d.is_empty_string()), colorize(d.is_dsclass())],
            ['e', repr(e), type(e.value), colorize(e.is_none()),
                colorize(e.is_empty_string()), colorize(e.is_dsclass())],
            ['f', repr(f), type(f.value), colorize(f.is_none()),
                colorize(f.is_empty_string()), colorize(f.is_dsclass())],
            ['g', repr(g), type(g.value), colorize(g.is_none()),
                colorize(g.is_empty_string()), colorize(g.is_dsclass())],
            ['h', repr(h), type(h.value), colorize(h.is_none()),
                colorize(h.is_empty_string()), colorize(h.is_dsclass())],
        ]

    equalities = [
            ['==', repr(a), repr(b), repr(c), repr(d), repr(e), repr(f),
                repr(g), repr(h)],
            [repr(a), colorize(a == a), colorize(a == b), colorize(a == c),
                colorize(a == d), colorize(a == e), colorize(a == f),
                colorize(a == g), colorize(a == h)],
            [repr(b), colorize(b == a), colorize(b == b), colorize(b == c),
                colorize(b == d), colorize(b == e), colorize(b == f),
                colorize(b == g), colorize(b == h)],
            [repr(c), colorize(c == a), colorize(c == b), colorize(c == c),
                colorize(c == d), colorize(c == e), colorize(c == f),
                colorize(c == g), colorize(c == h)],
            [repr(d), colorize(d == a), colorize(d == b), colorize(d == c),
                colorize(d == d), colorize(d == e), colorize(d == f),
                colorize(d == g), colorize(d == h)],
            [repr(e), colorize(e == a), colorize(e == b), colorize(e == c),
                colorize(e == d), colorize(e == e), colorize(e == f),
                colorize(e == g), colorize(e == h)],
            [repr(f), colorize(f == a), colorize(f == b), colorize(f == c),
                colorize(f == d), colorize(f == e), colorize(f == f),
                colorize(f == g), colorize(f == h)],
            [repr(g), colorize(g == a), colorize(g == b), colorize(g == c),
                colorize(g == d), colorize(g == e), colorize(g == f),
                colorize(g == g), colorize(g == h)],
            [repr(h), colorize(h == a), colorize(h == b), colorize(h == c),
                colorize(h == d), colorize(h == e), colorize(h == f),
                colorize(h == g), colorize(h == h)],
        ]

    inequalities = [
            ['!=', repr(a), repr(b), repr(c), repr(d), repr(e), repr(f),
                repr(g), repr(h)],
            [repr(a), colorize(a != a), colorize(a != b), colorize(a != c),
                colorize(a != d), colorize(a != e), colorize(a != f),
                colorize(a != g), colorize(a != h)],
            [repr(b), colorize(b != a), colorize(b != b), colorize(b != c),
                colorize(b != d), colorize(b != e), colorize(b != f),
                colorize(b != g), colorize(b != h)],
            [repr(c), colorize(c != a), colorize(c != b), colorize(c != c),
                colorize(c != d), colorize(c != e), colorize(c != f),
                colorize(c != g), colorize(c != h)],
            [repr(d), colorize(d != a), colorize(d != b), colorize(d != c),
                colorize(d != d), colorize(d != e), colorize(d != f),
                colorize(d != g), colorize(d != h)],
            [repr(e), colorize(e != a), colorize(e != b), colorize(e != c),
                colorize(e != d), colorize(e != e), colorize(e != f),
                colorize(e != g), colorize(e != h)],
            [repr(f), colorize(f != a), colorize(f != b), colorize(f != c),
                colorize(f != d), colorize(f != e), colorize(f != f),
                colorize(f != g), colorize(f != h)],
            [repr(g), colorize(g != a), colorize(g != b), colorize(g != c),
                colorize(g != d), colorize(g != e), colorize(g != f),
                colorize(g != g), colorize(g != h)],
            [repr(h), colorize(h != a), colorize(h != b), colorize(h != c),
                colorize(h != d), colorize(h != e), colorize(h != f),
                colorize(h != g), colorize(h != h)],
        ]

    less = [
            ['<', repr(a), repr(b), repr(c), repr(d), repr(e), repr(f),
                repr(g), repr(h)],
            [repr(a), colorize(a < a), colorize(a < b), colorize(a < c),
                colorize(a < d), colorize(a < e), colorize(a < f),
                colorize(a < g), colorize(a < h)],
            [repr(b), colorize(b < a), colorize(b < b), colorize(b < c),
                colorize(b < d), colorize(b < e), colorize(b < f),
                colorize(b < g), colorize(b < h)],
            [repr(c), colorize(c < a), colorize(c < b), colorize(c < c),
                colorize(c < d), colorize(c < e), colorize(c < f),
                colorize(c < g), colorize(c < h)],
            [repr(d), colorize(d < a), colorize(d < b), colorize(d < c),
                colorize(d < d), colorize(d < e), colorize(d < f),
                colorize(d < g), colorize(d < h)],
            [repr(e), colorize(e < a), colorize(e < b), colorize(e < c),
                colorize(e < d), colorize(e < e), colorize(e < f),
                colorize(e < g), colorize(e < h)],
            [repr(f), colorize(f < a), colorize(f < b), colorize(f < c),
                colorize(f < d), colorize(f < e), colorize(f < f),
                colorize(f < g), colorize(f < h)],
            [repr(g), colorize(g < a), colorize(g < b), colorize(g < c),
                colorize(g < d), colorize(g < e), colorize(g < f),
                colorize(g < g), colorize(g < h)],
            [repr(h), colorize(h < a), colorize(h < b), colorize(h < c),
                colorize(h < d), colorize(h < e), colorize(h < f),
                colorize(h < g), colorize(h < h)],
        ]

    greater = [
            ['>', repr(a), repr(b), repr(c), repr(d), repr(e), repr(f),
                repr(g), repr(h)],
            [repr(a), colorize(a > a), colorize(a > b), colorize(a > c),
                colorize(a > d), colorize(a > e), colorize(a > f),
                colorize(a > g), colorize(a > h)],
            [repr(b), colorize(b > a), colorize(b > b), colorize(b > c),
                colorize(b > d), colorize(b > e), colorize(b > f),
                colorize(b > g), colorize(b > h)],
            [repr(c), colorize(c > a), colorize(c > b), colorize(c > c),
                colorize(c > d), colorize(c > e), colorize(c > f),
                colorize(c > g), colorize(c > h)],
            [repr(d), colorize(d > a), colorize(d > b), colorize(d > c),
                colorize(d > d), colorize(d > e), colorize(d > f),
                colorize(d > g), colorize(d > h)],
            [repr(e), colorize(e > a), colorize(e > b), colorize(e > c),
                colorize(e > d), colorize(e > e), colorize(e > f),
                colorize(e > g), colorize(e > h)],
            [repr(f), colorize(f > a), colorize(f > b), colorize(f > c),
                colorize(f > d), colorize(f > e), colorize(f > f),
                colorize(f > g), colorize(f > h)],
            [repr(g), colorize(g > a), colorize(g > b), colorize(g > c),
                colorize(g > d), colorize(g > e), colorize(g > f),
                colorize(g > g), colorize(g > h)],
            [repr(h), colorize(h > a), colorize(h > b), colorize(h > c),
                colorize(h > d), colorize(h > e), colorize(h > f),
                colorize(h > g), colorize(h > h)],
        ]

    print('\n')
    print(fg('magenta_3b') + 'SliceLocation ' + attr('reset') + 'Class Tests')
    print('================================\n')
    print('Table I: Creation, Initialization and Methods Tests')
    print(tabulate(objects, headers='firstrow', tablefmt='psql'), '\n')
    print('Table II: Equality Tests')
    print(tabulate(equalities, headers='firstrow', tablefmt='psql'), '\n')
    print('Table II: Inequality Tests')
    print(tabulate(inequalities, headers='firstrow', tablefmt='psql'), '\n')
    print('Table III: Less Than Tests')
    print(tabulate(less, headers='firstrow', tablefmt='psql'), '\n')
    print('Table IV: Greater Than Tests')
    print(tabulate(greater, headers='firstrow', tablefmt='psql'), '\n')

    try:
        a == 'hello'
    except Exception as ex:
        print(ex)

    try:
        a != 5
    except Exception as ex:
        print(ex)

    try:
        a < 3.14
    except Exception as ex:
        print(ex)

    try:
        a > None
    except Exception as ex:
        print(ex)


def slice_shape_tests():
    a = SliceShape(512, 512)
    b = SliceShape(128, 256)
    c = SliceShape(512, 512)
    d = SliceShape(256, 128)

    slices = [
            ['a', 'b', 'c', 'd'],
            [str(a), str(b), str(c), str(d)]
        ]

    equalities = [
            ['==', str(a), str(b), str(c), str(d)],
            [str(a), colorize(a == a), colorize(a == b), colorize(a == c),
                colorize(a == d)],
            [str(b), colorize(b == a), colorize(b == b), colorize(b == c),
                colorize(b == d)],
            [str(c), colorize(c == a), colorize(c == b), colorize(c == c),
                colorize(c == d)],
            [str(d), colorize(d == a), colorize(d == b), colorize(d == c),
                colorize(d == d)],
        ]

    inequalities = [
            ['!=', str(a), str(b), str(c), str(d)],
            [str(a), colorize(a != a), colorize(a != b), colorize(a != c),
                colorize(a != d)],
            [str(b), colorize(b != a), colorize(b != b), colorize(b != c),
                colorize(b != d)],
            [str(c), colorize(c != a), colorize(c != b), colorize(c != c),
                colorize(c != d)],
            [str(d), colorize(d != a), colorize(d != b), colorize(d != c),
                colorize(d != d)],
        ]

    print('\n')
    print(fg('magenta_3b') + 'SliceShape ' + attr('reset') + 'Class Tests')
    print('================================\n')
    print('Table I: Initialization Tests')
    print(tabulate(slices, headers='firstrow', tablefmt='psql'), '\n')
    print('Table II: Equality Tests')
    print(tabulate(equalities, headers='firstrow', tablefmt='psql'), '\n')
    print('Table II: Inequality Tests')
    print(tabulate(inequalities, headers='firstrow', tablefmt='psql'), '\n')

    try:
        SliceShape('128', 128)
    except Exception as ex:
        print(ex)

    try:
        SliceShape(128, 128.0)
    except Exception as ex:
        print(ex)

    try:
        SliceShape('128', 128.0)
    except Exception as ex:
        print(ex)

    try:
        a == (512, 512)
    except Exception as ex:
        print(ex)

    try:
        a != 5
    except Exception as ex:
        print(ex)


def main():
    slice_location_tests()
    slice_shape_tests()


if __name__ == '__main__':
    main()
