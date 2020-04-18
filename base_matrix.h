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
void matrix_deallocate(MatrixObject *matrix);
MatrixObject *matrix_fill(int rows, int columns, double value);
void matrix_str(MatrixObject *matrix);

MatrixObject *matrix_random(int rows, int columns, int min, int max); /* not implemented */
MatrixObject *matrix_identity(int rows); /* not implemented */
MatrixObject *matrix_add(MatrixObject *matrix1, MatrixObject *matrix2); /* not implemented */
MatrixObject *matrix_dot(MatrixObject *matrix1, MatrixObject *matrix2); /* not implemented */
MatrixObject *matrix_mult(MatrixObject *matrix, int a); /* not implemented */
MatrixObject *matrix_transpose(MatrixObject *matrix); /* not implemented */
MatrixObject *matrix_row(int index); /* not implemented */
MatrixObject *matrix_column(int index); /* not implemented */
double matrix_det(MatrixObject *matrix); /* not implemented */
