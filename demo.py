#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    demo.py
    ~~~~~~~~~~~~~~

    A brief description goes here.
"""
import ctypes
from ctypes import c_int
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
    """
    vector is not an efficient way to build a list and return to python:
        http://stackoverflow.com/questions/16885344/how-to-handle-c-return-type-stdvectorint-in-python-ctypes
    """
    lib = ctypes.cdll.LoadLibrary("./cpp.so")
    lib.divide.restype = POINTER(c_int * 4) # so the result pointer will only iterate 4 times
    lib.divide.argtypes = [c_int, c_int]
    res = lib.divide(10, 3)
    for i in res.contents:
        print i


def get_numpy_array_pointer():
    x = numpy.array([3.14, 2.78, 1.4142356])
    # One should always specify the length of array
    l = len(x)
    len_p = c_int(l)
    # numpy default numerical is double type
    p = x.ctypes.data_as(POINTER(ctypes.c_double * len_p.value))
    print p
    for i in p.contents:
        print i

    # Besides, convert numpy array to ctypes array
    p = numpy.ctypeslib.as_ctypes(x)
    print p
    for i in p:
        print i


def main(argv):
    get_numpy_array_pointer()


if __name__ == '__main__':
    import sys
    main(sys.argv)
