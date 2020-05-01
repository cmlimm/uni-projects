#include "Python.h"
#include "matrix.h"
// #include "base_matrix.h"

static MatrixObject *PyObjectToMatrixObject(PyObject *pMatrix){
    PyObject *pMatrixSub;
    PyObject *pItem;
    Py_ssize_t rows, cols;
    MatrixObject *initial;
    int i, j;
    double item;

    rows = PyList_Size(pMatrix);
    pMatrixSub = PyList_GetItem(pMatrix, 0);
    cols = PyList_Size(pMatrixSub);

    initial = c_matrix_allocate(rows, cols);
    for (i = 0; i < rows; i++) {
        pMatrixSub = PyList_GetItem(pMatrix, i);

        for (j = 0; j < cols; j++) {
            pItem = PyList_GetItem(pMatrixSub, j);

            if(!PyFloat_Check(pItem)){
                PyErr_SetString(PyExc_ValueError, "List items must by float.");
                return NULL;
            }

            item = PyFloat_AsDouble(pItem);
            initial->values[i][j] = item;
        }
    }

    return initial;
}

static PyObject *MatrixObjectToPyObject(MatrixObject* matrix){
    PyObject *pList, *pSublist;
    PyObject *pItem;
    Py_ssize_t rows, cols;
    int i, j;

    rows = matrix->rows;
    cols = matrix->columns;

    pList = PyList_New(rows);
    for (i = 0; i < rows; i++) {
        pSublist = PyList_New(cols);
        for (j = 0; j < cols; j++) {
            pItem = Py_BuildValue("d", matrix->values[i][j]);
            PyList_SetItem(pSublist, j, pItem);
        }
        PyList_SetItem(pList, i, pSublist);
    }

    return pList;
}

static PyObject *fill(PyObject *self, PyObject *args){
    PyObject *pValue;
    PyObject *pList;
    PyObject *pSublist;
    int i, j, rows, cols;
    double value;

    if (!PyArg_ParseTuple(args, "iid", &rows, &cols, &value)) {
        PyErr_SetString(PyExc_TypeError, "Parameters must be (int, int, float).");
        return NULL;
    }

    pValue = Py_BuildValue("d", value);

    pList = PyList_New(rows);
    for (i = 0; i < rows; i++) {
        pSublist = PyList_New(cols);
        for (j = 0; j < cols; j++) {
            PyList_SetItem(pSublist, j, pValue);
        }
        PyList_SetItem(pList, i, pSublist);
    }

    return pList;
}

static PyObject *randfill(PyObject *self, PyObject *args){
    PyObject *pValue;
    PyObject *pList;
    PyObject *pSublist;
    int i, j, rows, cols;
    double min, max;

    srand(time(NULL));

    if (!PyArg_ParseTuple(args, "iidd", &rows, &cols, &min, &max)) {
        PyErr_SetString(PyExc_TypeError, "Parameters must be (int, int, float, float).");
        return NULL;
    }

    pList = PyList_New(rows);
    for (i = 0; i < rows; i++) {
        pSublist = PyList_New(cols);
        for (j = 0; j < cols; j++) {
            pValue = Py_BuildValue("d", RandomReal(min, max));
            PyList_SetItem(pSublist, j, pValue);
        }
        PyList_SetItem(pList, i, pSublist);
    }

    return pList;
}

static PyObject *identity(PyObject *self, PyObject *args){
    PyObject *pOne, *pZero;
    PyObject *pList;
    PyObject *pSublist;
    int i, j, rows;

    if (!PyArg_ParseTuple(args, "i", &rows)) {
        PyErr_SetString(PyExc_TypeError, "Parameter must be int.");
        return NULL;
    }

    pOne = Py_BuildValue("d", 1.0);
    pZero = Py_BuildValue("d", 0.0);

    pList = PyList_New(rows);
    for (i = 0; i < rows; i++) {
        pSublist = PyList_New(rows);
        for (j = 0; j < rows; j++) {
            if (i == j)
                PyList_SetItem(pSublist, j, pOne);
            else
                PyList_SetItem(pSublist, j, pZero);
        }
        PyList_SetItem(pList, i, pSublist);
    }

    return pList;
}

static PyObject* matrix_add(PyObject *self, PyObject *args){
    return matrix_add_common(self, args, 1);
}

static PyObject* matrix_sub(PyObject *self, PyObject *args){
    return matrix_add_common(self, args, -1);
}

static PyObject* matrix_add_common(PyObject *self, PyObject *args, int sign){
    PyObject *pMatrix1, *pMatrix2;
    PyObject *pMatrixSub1, *pMatrixSub2;
    PyObject *pItem1, *pItem2, *pItem;
    PyObject *pList, *pSublist;
    Py_ssize_t rows1, rows2, cols1, cols2;
    int i, j;
    float item1, item2, item;

    if (!PyArg_ParseTuple(args, "O!O!", &PyList_Type, &pMatrix1, &PyList_Type, &pMatrix2)) {
        PyErr_SetString(PyExc_TypeError, "Parameters must be (list, list).");
        return NULL;
    }

    rows1 = PyList_Size(pMatrix1);
    rows2 = PyList_Size(pMatrix2);
    if(rows1 != rows2) {
        PyErr_SetString(PyExc_ValueError, "Shapes of the matrixes must be the same.");
        return NULL;
    }

    pList = PyList_New(rows1);
    for (i = 0; i < rows1; i++) {
        pMatrixSub1 = PyList_GetItem(pMatrix1, i);
        pMatrixSub2 = PyList_GetItem(pMatrix2, i);

        cols1 = PyList_Size(pMatrixSub1);
        cols2 = PyList_Size(pMatrixSub1);

        if(cols1 != cols2) {
            PyErr_SetString(PyExc_ValueError, "Shapes of the matrixes must be the same.");
            return NULL;
        }

        pSublist = PyList_New(cols1);
        for (j = 0; j < cols1; j++) {
            pItem1 = PyList_GetItem(pMatrixSub1, j);
            pItem2 = PyList_GetItem(pMatrixSub2, j);

            if(!PyFloat_Check(pItem1) && !PyFloat_Check(pItem2)){
                PyErr_SetString(PyExc_ValueError, "List items must by float.");
                return NULL;
            }

            item1 = PyFloat_AsDouble(pItem1);
            item2 = PyFloat_AsDouble(pItem2);
            item = item1 + sign*item2;

            pItem = Py_BuildValue("d", item);
            PyList_SetItem(pSublist, j, pItem);
        }
        PyList_SetItem(pList, i, pSublist);
    }

    return pList;
}

static PyObject* matrix_transpose(PyObject *self, PyObject *args) {
    PyObject *pMatrix, *pList;
    MatrixObject *initial, *result;

    if (!PyArg_ParseTuple(args, "O!", &PyList_Type, &pMatrix)) {
        PyErr_SetString(PyExc_TypeError, "Parameter must be a list.");
        return NULL;
    }

    initial = PyObjectToMatrixObject(pMatrix);
    result = c_matrix_transpose(initial);
    pList = MatrixObjectToPyObject(result);

    c_matrix_deallocate(initial);
    c_matrix_deallocate(result);
    return pList;
}

static PyMethodDef MatrixMethods[] = {
    {"fill", (PyCFunction)fill, METH_VARARGS,
     "Returns matrix filled with certain value"},
    {"randfill", (PyCFunction)randfill, METH_VARARGS,
     "Returns matrix filled with random values"},
    {"identity", (PyCFunction)identity, METH_VARARGS,
     "Returns identity matrix"},
    {"add", (PyCFunction)matrix_add, METH_VARARGS,
     "Adds two matrixes"},
    {"sub", (PyCFunction)matrix_sub, METH_VARARGS,
     "Subtracts one matrix from another"},
    {"transpose", (PyCFunction)matrix_transpose, METH_VARARGS,
     "Transposes matrix"},
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

    m = PyModule_Create(&matrixmanmodule);
    if (m == NULL)
        return NULL;

    return m;
}
