#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "Python.h"
#include "arrayobject.h"

PyArrayObject *array=NULL;

/* Method of the python object */
PyObject *get_global_numpy_array(PyObject *self, PyObject *args){
    printf("starting...\n");
    if (!array) {
        npy_intp dim[2] = {3, 3};
        npy_intp dim1[1];
        dim1[0] = 10;
        printf("fucking...\n");
        array = (PyArrayObject *)PyArray_SimpleNew(1, dim1, NPY_INT);
        printf("assigning...\n");
        int *buffer = (int*)array->data;
        int i;
        for (i=0; i<3*3; i++) {
            buffer[i] = i;
        }
        printf("finish initializing exiting...\n");
    }
    printf("exiting...\n");
    return (PyObject *)array;
}

