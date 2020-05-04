#include "../c/base_matrix.h"

static MatrixObject *PyListToMatrixObject(PyObject *pMatrix);
static PyObject *MatrixObjectToPyList(MatrixObject* matrix);
static PyObject* fill(PyObject *self, PyObject *args);
static PyObject* randfill(PyObject *self, PyObject *args);
static PyObject* identity(PyObject *self, PyObject *args);
static PyObject* matrix_add(PyObject *self, PyObject *args);
static PyObject* matrix_sub(PyObject *self, PyObject *args);
static PyObject* matrix_transpose(PyObject *self, PyObject *args);
static PyObject* matrix_mult(PyObject *self, PyObject *args);
static PyObject* matrix_negative(PyObject *self, PyObject *args);
static PyObject* matrix_dot(PyObject *self, PyObject *args);

PyMODINIT_FUNC PyInit_matrixman(void);
