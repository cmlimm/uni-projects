#include "Python.h"
#include "matrix.h"

static MatrixObject *
fill(PyObject *args){
    MatrixObject *result;
    int check;
    int rows, cols;
    double value;

    check = PyArg_ParseTuple(args, "iid", &rows, &cols, &value);
    if (!check){
        return NULL;/* implement error?*/
    }

    result = c_matrix_fill(rows, cols, value);

    return result;
}

// static PyNumberMethods matrix_as_number = {
//     .nb_add = (binaryfunc) matrix_add
//     .nb_sub = (binaryfunc) matrix_sub
//     .nb_multiply = (binaryfunc) matrix_mult
//     .nb_neg = (unaryfunc) matrix_negative
// }
//
// static PySequenceMethods matrix_as_sequence = {
//     .sq_item = (ssizeargfunc)matrix_item
// }

static PyTypeObject MatrixType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "matrixman.MatrixObject",
    .tp_doc = "Matrix objects",
    .tp_basicsize = sizeof(MatrixObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = PyType_GenericNew,
    // .tp_dealloc = (destructor) matrix_dealloc,
    // .tp_print = (reprfunc) matrix_str
    // .tp_as_number = &matrix_as_number
    // .tp_as_sequence = &matrix_as_sequence
    // .tp_methods = Matrix_methods,
};

static PyMethodDef MatrixMethods[] = {
    {"fill", (PyCFunction)fill, METH_VARARGS,
     "Returns matrix of specified size filled with one certain value"},
    // {"random", random, METH_VARARGS,
    //  "Returns matrix of specified size filled with random values"},
    // {"identity", identity, METH_VARARGS,
    //  "Return identity matrix of specified size"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef matrixmanmodule = {
    PyModuleDef_HEAD_INIT,
    .m_name = "matrixman",
    .m_doc = "Module dedicated to working with matrixes",
    .m_size = -1,
    .m_methods = MatrixMethods
};

PyMODINIT_FUNC PyInit_matrixman(void)
{
    PyObject *m;
    if (PyType_Ready(&MatrixType) < 0)
        return NULL;

    m = PyModule_Create(&matrixmanmodule);
    if (m == NULL)
        return NULL;

    Py_INCREF(&MatrixType);
    if (PyModule_AddObject(m, "Matrix", (PyObject *) &MatrixType) < 0) {
        Py_DECREF(&MatrixType);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}
