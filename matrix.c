#include <Python.h>
#include "matrix.h"
#include "base_matrix.h"

static PyTypeObject MatrixType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "matrixman.MatrixObject",
    .tp_doc = "Matrix objects",
    .tp_basicsize = sizeof(MatrixObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = PyType_GenericNew,
    .tp_dealloc = (destructor) matrix_dealloc,
    .tp_methods = Matrix_methods,
};

static PyMethodDef MatrixMethods[] = {
    {"fill", fill, METH_VARARGS,
     "Returns matrix of specified size filled with one certain value"},
    {"random", random, METH_VARARGS,
     "Returns matrix of specified size filled with random values"},
    {"identity", identity, METH_VARARGS,
     "Return identity matrix of specified size"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef matrixman = {
    PyModuleDef_HEAD_INIT,
    "matrixman",
    "Module dedicated to working with matrixes",
    -1,
    MatrixMethods
};

PyMODINIT_FUNC PyInit_matrixman(void)
{
    return PyModule_Create(&matrixman);
}
