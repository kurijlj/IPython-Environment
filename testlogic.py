#!/usr/bin/env python

def testlogic(x, y, logic):
    for a in x:
        for b in y:
            print(a, b, logic(a, b))


def logica(x, y):
    return bool(x == y)

