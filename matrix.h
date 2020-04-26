#include <Python.h>
#include "base_matrix.h"

typedef struct MatrixObject{
    PyObject_HEAD
    int rows;
    int columns;
    double **values;
} MatrixObject;

static PyTypeObject MatrixType;
static PyObject* matrix_allocate(PyObject *args);
static void Matrix_dealloc(MatrixObject *matrix);
static PyObject* str(MatrixObject *matrix);
static PyObject* fill(PyObject *args);
static PyObject* random(PyObject *args);
static PyObject* identity(PyObject *args);
static PyObject* add(MatrixObject *matrix1, MatrixObject *matrix2);
static PyObject* mult(MatrixObject *matrix, PyObject *args);
static PyObject* negative(MatrixObject *matrix);
static PyObject* sub(MatrixObject *matrix1, MatrixObject *matrix2);
static PyObject* transpose(MatrixObject *matrix);
static PyObject* dot(MatrixObject *matrix1, MatrixObject *matrix2);

PyMODINIT_FUNC PyInit_matrixmanipulate(void)
