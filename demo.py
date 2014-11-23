#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    demo.py
    ~~~~~~~~~~~~~~

    A brief description goes here.
"""
import ctypes
from ctypes import c_char_p
from ctypes import c_void_p

import numpy


def get(key):
    pass


def set(key, value):
    pass


def delete(key):
    pass


def foo():
    ll = ctypes.cdll.LoadLibrary
    lib = ll("./ctype.so")
    #lib.set.restype = c_char
    lib.set.restype = c_char_p
    lib.set.argtypes = [c_char_p]
    a = numpy.array([1, 2, 3])
    l = a.tostring()
    l = "abcdef"
    res = lib.set(l)
    print res
    #new_array = numpy.fromstring(res, dtype=int)


def main(argv):
    foo()


if __name__ == '__main__':
    import sys
    main(sys.argv)
