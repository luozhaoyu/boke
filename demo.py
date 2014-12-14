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


def modify_int_array():
    """Deliver C pointer to Python
    vector is not an efficient way to build a list and return to python:
        http://stackoverflow.com/questions/16885344/how-to-handle-c-return-type-stdvectorint-in-python-ctypes
    """
    lib = ctypes.cdll.LoadLibrary("./cpp.so")
    lib.get_global_array.restype = POINTER(c_int * 4) # so the result pointer will only iterate 4 times
    lib.get_global_array.argtypes = [c_int, c_int]
    ptr = lib.get_global_array(10, 3)
    print [i for i in ptr.contents]
    # change the global array's value
    ptr.contents[2] = 100

    ptr1 = lib.get_global_array(10, 3)
    print [i for i in ptr1.contents]


def modify_numpy_array():
    """Deliver C pointer to Python

    TODO: anaconda's numpy C source version pops warning since it is not 1.9
    """
    get_global_numpy_array = ctypes.cdll.LoadLibrary("./ctype.so").get_global_numpy_array
    #get_global_numpy_array.restype = [] # so the result pointer will only iterate 4 times
    #get_global_numpy_array.argtypes = [c_int, c_int]
    ptr = get_global_numpy_array()
    return ptr


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
    modify_numpy_array()


if __name__ == '__main__':
    import sys
    main(sys.argv)
