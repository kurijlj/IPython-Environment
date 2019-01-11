#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tester.py

try:
    from pydicom.valuerep import DSdecimal, DSfloat
except ImportError:
    from dicom.valuerep import DSdecimal, DSfloat
from tabulate import tabulate
from dds import SliceLocation


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

    objects = [
            ['variable', 'value', 'type', 'is None', 'is empty string',
                'is DSclass'],
            ['a', repr(a), type(a.value), a.is_none(), a.is_empty_string(),
                a.is_dsclass()],
            ['b', repr(b), type(b.value), b.is_none(), b.is_empty_string(),
                b.is_dsclass()],
            ['c', repr(c), type(c.value), c.is_none(), c.is_empty_string(),
                c.is_dsclass()],
            ['d', repr(d), type(d.value), d.is_none(), d.is_empty_string(),
                d.is_dsclass()],
            ['e', repr(e), type(e.value), e.is_none(), e.is_empty_string(),
                e.is_dsclass()],
            ['f', repr(f), type(f.value), f.is_none(), f.is_empty_string(),
                f.is_dsclass()],
            ['g', repr(g), type(g.value), g.is_none(), g.is_empty_string(),
                g.is_dsclass()],
            ['h', repr(h), type(h.value), h.is_none(), h.is_empty_string(),
                h.is_dsclass()],
        ]

    equalities = [
            ['==', repr(a), repr(b), repr(c), repr(d), repr(e), repr(f),
                repr(g), repr(h)],
            [repr(a), a == a, a == b, a == c, a == d, a == e, a == f, a == g,
                a == h],
            [repr(b), b == a, b == b, b == c, b == d, b == e, b == f, b == g,
                b == h],
            [repr(c), c == a, c == b, c == c, c == d, c == e, c == f, c == g,
                c == h],
            [repr(d), d == a, d == b, d == c, d == d, d == e, d == f, d == g,
                d == h],
            [repr(e), e == a, e == b, e == c, e == d, e == e, e == f, e == g,
                e == h],
            [repr(f), f == a, f == b, f == c, f == d, f == e, f == f, f == g,
                f == h],
            [repr(g), g == a, g == b, g == c, g == d, g == e, g == f, g == g,
                g == h],
            [repr(h), h == a, h == b, h == c, h == d, h == e, h == f, h == g,
                h == h],
        ]

    inequalities = [
            ['!=', repr(a), repr(b), repr(c), repr(d), repr(e), repr(f),
                repr(g), repr(h)],
            [repr(a), a != a, a != b, a != c, a != d, a != e, a != f, a != g,
                a != h],
            [repr(b), b != a, b != b, b != c, b != d, b != e, b != f, b != g,
                b != h],
            [repr(c), c != a, c != b, c != c, c != d, c != e, c != f, c != g,
                c != h],
            [repr(d), d != a, d != b, d != c, d != d, d != e, d != f, d != g,
                d != h],
            [repr(e), e != a, e != b, e != c, e != d, e != e, e != f, e != g,
                e != h],
            [repr(f), f != a, f != b, f != c, f != d, f != e, f != f, f != g,
                f != h],
            [repr(g), g != a, g != b, g != c, g != d, g != e, g != f, g != g,
                g != h],
            [repr(h), h != a, h != b, h != c, h != d, h != e, h != f, h != g,
                h != h],
        ]

    print('Table I: Objects')
    print(tabulate(objects, headers='firstrow', tablefmt='psql'), '\n')
    print('Table II: Equalities')
    print(tabulate(equalities, headers='firstrow', tablefmt='psql'), '\n')
    print('Table II: Inequalities')
    print(tabulate(inequalities, headers='firstrow', tablefmt='psql'), '\n')


if __name__ == '__main__':
    main()
