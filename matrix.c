#include <Python.h>
#include "matrix.h"
#include "base_matrix.h"

static PyTypeObject MatrixType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "matrixmanipulate.MatrixObject",
    .tp_doc = "Matrix objects",
    .tp_basicsize = sizeof(MatrixObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = Matrix_new,
    .tp_init = (initproc) Matrix_init,
    .tp_dealloc = (destructor) Matrix_dealloc,
    .tp_methods = Matrix_methods,
};

PyMODINIT_FUNC PyInit_matrixmanipulate(void)
{
    return PyModule_Create(&matrixmaniplulatemodule);
}

static struct PyModuleDef matrixmaniplulatemodule = {
    PyModuleDef_HEAD_INIT,
    "matrixmanipulate",   /* name of module */
    "Module dedicated to working with matrixes", /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    matrixmanipulatemethods
};
