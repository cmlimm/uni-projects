#define MAX_MATRIX_SIZE = 256;

/*
 * Struct: matrix
 * ----------------
 * rows: integer number of rows
 * columns: integer number of columns
 * values: 2-dimensional array of double values in matrix
 */
typedef struct MatrixObject{
    int rows;
    int columns;
    double **values;
} MatrixObject;

MatrixObject *matrix_allocate(int rows, int columns);
void matrix_deallocate(MatrixObject *mtrx);
MatrixObject *matrix_fill(int rows, int columns, double value);
void matrix_show(MatrixObject *mtrx);

MatrixObject *matrix_random(int rows, int columns, int min, int max); /* not implemented */
MatrixObject *matrix_identity(int rows); /* not implemented */
MatrixObject *matrix_add(MatrixObject *mtrx1, MatrixObject *mtrx2); /* not implemented */
MatrixObject *matrix_dot(MatrixObject *mtrx1, MatrixObject *mtrx2); /* not implemented */
MatrixObject *matrix_mult(MatrixObject *mtrx1, int a); /* not implemented */
MatrixObject *matrix_transpose(MatrixObject *mtrx1); /* not implemented */
MatrixObject *matrix_row(int index); /* not implemented */
MatrixObject *matrix_column(int index); /* not implemented */
double matrix_det(MatrixObject *mtrx); /* not implemented */
