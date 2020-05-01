#include "base_matrix.h"

static MatrixObject *PyObjectToMatrixObject(PyObject *pMatrix);
static PyObject *MatrixObjectToPyObject(MatrixObject* matrix);
static PyObject* fill(PyObject *self, PyObject *args);
static PyObject* randfill(PyObject *self, PyObject *args);
static PyObject* identity(PyObject *self, PyObject *args);
static PyObject* matrix_add_common(PyObject *self, PyObject *args, int sign);
static PyObject* matrix_add(PyObject *self, PyObject *args);
static PyObject* matrix_sub(PyObject *self, PyObject *args);
static PyObject* matrix_transpose(PyObject *self, PyObject *args);
// static PyObject* matrix_mult(MatrixObject *matrix, PyObject *args);
// static PyObject* matrix_negative(MatrixObject *matrix);
// static PyObject* matrix_dot(MatrixObject *matrix1, MatrixObject *matrix2);

PyMODINIT_FUNC PyInit_matrixman(void);
