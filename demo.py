#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    demo.py
    ~~~~~~~~~~~~~~

    A brief description goes here.
"""
import ctypes
from ctypes import c_void_p, c_int, c_int, c_char_p
from ctypes import POINTER

import numpy


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


def divide():
    lib = ctypes.cdll.LoadLibrary("./cpp.so")
    lib.divide.restype = POINTER(c_int * 4) # so the result pointer will only iterate 4 times
    lib.divide.argtypes = [c_int, c_int]
    res = lib.divide(10, 3)
    for i in res.contents:
        print i


def main(argv):
    divide()


if __name__ == '__main__':
    import sys
    main(sys.argv)
