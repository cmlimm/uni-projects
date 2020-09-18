#include "Python.h"
#include "matrix.h"

/*
 * Function: PyListToMatrixObject
 * --------------------------------
 * converts PyList to MatrixObject
 *
 * returns: MatrixObject
 */
static MatrixObject *PyListToMatrixObject(PyObject *pMatrix){
    PyObject *pMatrixSub;
    PyObject *pItem;
    Py_ssize_t rows, cols, tempCols;
    MatrixObject *matrix;
    int i, j;
    double item;

    rows = PyList_Size(pMatrix);
    // get first row and calculate it's length
    pMatrixSub = PyList_GetItem(pMatrix, 0);
    cols = PyList_Size(pMatrixSub);

    // allocate memory for MatrixObject
    matrix = c_matrix_allocate(rows, cols);
    for (i = 0; i < rows; i++) {
        // get i_th row
        pMatrixSub = PyList_GetItem(pMatrix, i);
        tempCols = PyList_Size(pMatrixSub);

        // check dimensions
        if(tempCols != cols){
            PyErr_SetString(PyExc_ValueError, "Matrixes must have the same dimensions.");
            return NULL;
        }

        for (j = 0; j < cols; j++) {
            // get pMatrix[i][j]
            pItem = PyList_GetItem(pMatrixSub, j);
            if(!PyFloat_Check(pItem)){
                PyErr_SetString(PyExc_TypeError, "List items must be float.");
                return NULL;
            }

            item = PyFloat_AsDouble(pItem);
            matrix->values[i][j] = item;
        }
    }

    return matrix;
}

/*
 * Function: MatrixObjectToPyList
 * --------------------------------
 * converts MatrixObject to PyList
 *
 * returns: PyList
 */
static PyObject *MatrixObjectToPyList(MatrixObject* matrix){
    PyObject *pList, *pSublist;
    PyObject *pItem;
    Py_ssize_t rows, cols;
    int i, j;

    // get dimensions of matrix
    rows = matrix->rows;
    cols = matrix->columns;

    // create main list with empty rows
    pList = PyList_New(rows);
    for (i = 0; i < rows; i++) {
        // create row
        pSublist = PyList_New(cols);
        for (j = 0; j < cols; j++) {
            // write MatrixObject[i][j] to PyList[i][j]
            pItem = Py_BuildValue("d", matrix->values[i][j]);
            PyList_SetItem(pSublist, j, pItem);
        }
        // write row to Pylist
        PyList_SetItem(pList, i, pSublist);
    }

    return pList;
}

/*
 * Function: fill
 * --------------
 * fills PyList with specified value
 *
 * returns: PyList
 */
static PyObject *fill(PyObject *self, PyObject *args){
    MatrixObject *matrix;
    PyObject *pList;
    int rows, cols;
    double value;

    // check parameters
    if (!PyArg_ParseTuple(args, "iid", &rows, &cols, &value)) {
        PyErr_SetString(PyExc_TypeError, "Parameters must be (int, int, float).");
        return NULL;
    }

    matrix = c_matrix_fill(rows, cols, value);
    pList = MatrixObjectToPyList(matrix);

    c_matrix_deallocate(matrix);

    return pList;
}

/*
 * Function: randfill
 * ------------------
 * fills PyList with random values
 *
 * returns: PyList
 */
static PyObject *randfill(PyObject *self, PyObject *args){
    MatrixObject *matrix;
    PyObject *pList;
    int rows, cols;
    double min, max;

    //check parameters
    if (!PyArg_ParseTuple(args, "iidd", &rows, &cols, &min, &max)) {
        PyErr_SetString(PyExc_TypeError, "Parameters must be (int, int, float, float).");
        return NULL;
    }

    matrix = c_matrix_random(rows, cols, min, max);
    pList = MatrixObjectToPyList(matrix);

    c_matrix_deallocate(matrix);

    return pList;
}

/*
 * Function: identity
 * ------------------
 * creates identity matrix in form of Pylist
 *
 * returns: PyList
 */
static PyObject *identity(PyObject *self, PyObject *args){
    MatrixObject *matrix;
    PyObject *pList;
    int rows;

    //check parameters
    if (!PyArg_ParseTuple(args, "i", &rows)) {
        PyErr_SetString(PyExc_TypeError, "Parameter must be int.");
        return NULL;
    }

    matrix = c_matrix_identity(rows);
    pList = MatrixObjectToPyList(matrix);

    c_matrix_deallocate(matrix);

    return pList;
}

/*
 * Function: add
 * -------------
 * sums two Pylist like matrixes
 * args: [[1.0, 1.0],[2.0, 2.0]], [[2.0, 2.0],[1.0, 1.0]]
 * result: [[3.0, 3.0],[3.0, 3.0]]
 *
 * returns: PyList
 */
static PyObject* matrix_add(PyObject *self, PyObject *args){
    PyObject *pMatrix1, *pMatrix2;
    MatrixObject *matrix1, *matrix2;
    MatrixObject *result;
    PyObject *pList;

    // check parameters
    if (!PyArg_ParseTuple(args, "O!O!", &PyList_Type, &pMatrix1, &PyList_Type, &pMatrix2)) {
        PyErr_SetString(PyExc_TypeError, "Parameters must be (list, list).");
        return NULL;
    }

    matrix1 = PyListToMatrixObject(pMatrix1);
    if (matrix1 == NULL && PyErr_Occurred()) {
        PyErr_SetString(PyExc_TypeError, "List items must be float.");
        return NULL;
    }

    matrix2 = PyListToMatrixObject(pMatrix2);
    if (matrix2 == NULL && PyErr_Occurred()) {
        PyErr_SetString(PyExc_TypeError, "List items must be float.");
        return NULL;
    }
    if ((matrix1->rows != matrix2->rows) || (matrix1->columns != matrix2->columns)) {
        PyErr_SetString(PyExc_ValueError, "Matrixes must have the same dimensions.");
        return NULL;
    }

    result = c_matrix_add(matrix1, matrix2);
    pList = MatrixObjectToPyList(result);

    return pList;
}

/*
 * Function: sub
 * -------------
 * subtracts two Pylist like matrixes
 * args: [[1.0, 1.0],[2.0, 2.0]], [[2.0, 2.0],[1.0, 1.0]]
 * result: [[-1.0, -1.0],[1.0, 1.0]]
 *
 * returns: PyList
 */
static PyObject* matrix_sub(PyObject *self, PyObject *args){
    PyObject *pMatrix1, *pMatrix2;
    MatrixObject *matrix1, *matrix2;
    MatrixObject *result;
    PyObject *pList;

    // check parameters
    if (!PyArg_ParseTuple(args, "O!O!", &PyList_Type, &pMatrix1, &PyList_Type, &pMatrix2)) {
        PyErr_SetString(PyExc_TypeError, "Parameters must be (list, list).");
        return NULL;
    }

    matrix1 = PyListToMatrixObject(pMatrix1);
    if (matrix1 == NULL && PyErr_Occurred()) {
        PyErr_SetString(PyExc_TypeError, "List items must be float.");
        return NULL;
    }

    matrix2 = PyListToMatrixObject(pMatrix2);
    if (matrix2 == NULL && PyErr_Occurred()) {
        PyErr_SetString(PyExc_TypeError, "List items must be float.");
        return NULL;
    }

    if ((matrix1->rows != matrix2->rows) || (matrix1->columns != matrix2->columns)) {
        PyErr_SetString(PyExc_ValueError, "Matrixes must have the same dimensions.");
        return NULL;
    }
    result = c_matrix_sub(matrix1, matrix2);
    pList = MatrixObjectToPyList(result);

    return pList;
}

/*
 * Function: transpose
 * -------------------
 * transposes PyList like matrix
 * args: [[1.0, 2.0],
 *        [3.0, 4.0]]
 * result: [[1.0, 3.0],
 *          [2.0, 4.0]]
 *
 * returns: PyList
 */
static PyObject* matrix_transpose(PyObject *self, PyObject *args) {
    PyObject *pMatrix, *pList;
    MatrixObject *initial, *result;

    // check parameters
    if (!PyArg_ParseTuple(args, "O!", &PyList_Type, &pMatrix)) {
        PyErr_SetString(PyExc_TypeError, "Parameter must be a list.");
        return NULL;
    }

    initial = PyListToMatrixObject(pMatrix);
    if (initial == NULL && PyErr_Occurred()) {
        PyErr_SetString(PyExc_TypeError, "List items must be float.");
        return NULL;
    }

    result = c_matrix_transpose(initial);
    pList = MatrixObjectToPyList(result);

    c_matrix_deallocate(initial);
    c_matrix_deallocate(result);
    return pList;
}

/*
 * Function: mult
 * --------------
 * multiply PyLists by float
 *
 * returns: PyList
 */
static PyObject *matrix_mult(PyObject *self, PyObject *args){
    MatrixObject *initial, *result;
    PyObject *pMatrix, *pList;
    double value;

    // check parameters
    if (!PyArg_ParseTuple(args, "O!d", &PyList_Type, &pMatrix, &value)) {
        PyErr_SetString(PyExc_TypeError, "Parameters must be (list, float).");
        return NULL;
    }

    initial = PyListToMatrixObject(pMatrix);
    if (initial == NULL && PyErr_Occurred()) {
        PyErr_SetString(PyExc_TypeError, "List items must be float.");
        return NULL;
    }

    result = c_matrix_mult(initial, value);
    pList = MatrixObjectToPyList(result);

    c_matrix_deallocate(initial);
    c_matrix_deallocate(result);

    return pList;
}

/*
 * Function: negative
 * ------------------
 * multiply every element of the PyList by -1
 *
 * returns: PyList
 */
static PyObject *matrix_negative(PyObject *self, PyObject *args){
    MatrixObject *initial, *result;
    PyObject *pMatrix, *pList;

    // check parameters
    if (!PyArg_ParseTuple(args, "O!", &PyList_Type, &pMatrix)) {
        PyErr_SetString(PyExc_TypeError, "Parameter must be (list).");
        return NULL;
    }

    initial = PyListToMatrixObject(pMatrix);
    if (initial == NULL && PyErr_Occurred()) {
        PyErr_SetString(PyExc_TypeError, "List items must be float.");
        return NULL;
    }

    result = c_matrix_negative(initial);
    pList = MatrixObjectToPyList(result);

    c_matrix_deallocate(initial);
    c_matrix_deallocate(result);

    return pList;
}

/*
 * Function: dot
 * -------------------
 * PyList1.PyList2
 *
 * returns: PyList
 */
static PyObject* matrix_dot(PyObject *self, PyObject *args){
    PyObject *pMatrix1, *pMatrix2;
    MatrixObject *matrix1, *matrix2;
    MatrixObject *result;
    PyObject *pList;

    // check parameters
    if (!PyArg_ParseTuple(args, "O!O!", &PyList_Type, &pMatrix1, &PyList_Type, &pMatrix2)) {
        PyErr_SetString(PyExc_TypeError, "Parameters must be (list, list).");
        return NULL;
    }

    matrix1 = PyListToMatrixObject(pMatrix1);
    if (matrix1 == NULL && PyErr_Occurred()) {
        PyErr_SetString(PyExc_TypeError, "List items must be float.");
        return NULL;
    }

    matrix2 = PyListToMatrixObject(pMatrix2);
    if (matrix2 == NULL && PyErr_Occurred()) {
        PyErr_SetString(PyExc_TypeError, "List items must be float.");
        return NULL;
    }

    if (matrix1->columns != matrix2->rows) {
        PyErr_SetString(PyExc_ValueError, "Number of columns of the first matrix must be the same as number of rows of the second matrix.");
        return NULL;
    }
    result = c_matrix_dot(matrix1, matrix2);
    pList = MatrixObjectToPyList(result);

    return pList;
}

static PyMethodDef MatrixMethods[] = {
    //{"name of function", function, type of args, doc string}
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
    {"mult", (PyCFunction)matrix_mult, METH_VARARGS,
     "Mult matrix by the number"},
    {"negative", (PyCFunction)matrix_negative, METH_VARARGS,
     "Mult matrix by -1"},
    {"dot", (PyCFunction)matrix_dot, METH_VARARGS,
     "Dot product of two matrixes"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef matrixmanmodule = {
    PyModuleDef_HEAD_INIT, // ???
    .m_name = "matrixman", // mosule name
    .m_doc = "Module dedicated to working with matrixes", // doc string
    .m_size = -1, // ???
    .m_methods = MatrixMethods // struct with methods
};

PyMODINIT_FUNC PyInit_matrixman(void)
{
    PyObject *m;

    m = PyModule_Create(&matrixmanmodule);
    if (m == NULL)
        return NULL;

    return m;
}
