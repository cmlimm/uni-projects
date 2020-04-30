#include "base_matrix.h"

static PyTypeObject MatrixType;
/*static PyObject* matrix_alloc(PyObject *args);*/
// void matrix_dealloc(MatrixObject *matrix);
// static PyObject* str(MatrixObject *matrix);
static MatrixObject* fill(PyObject *args);
// static PyObject* random(PyObject *args);
// static PyObject* identity(PyObject *args);
// static PyObject* matrix_transpose(MatrixObject *matrix);
// static PyObject* matrix_add(MatrixObject *matrix1, MatrixObject *matrix2);
// static PyObject* matrix_mult(MatrixObject *matrix, PyObject *args);
// static PyObject* matrix_negative(MatrixObject *matrix);
// static PyObject* matrix_sub(MatrixObject *matrix1, MatrixObject *matrix2);
// static PyObject* matrix_dot(MatrixObject *matrix1, MatrixObject *matrix2);

PyMODINIT_FUNC PyInit_matrixman(void);
