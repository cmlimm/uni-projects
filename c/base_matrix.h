#define MAX_c_matrix_SIZE = 256;

/*
 * Constant: RAND_MAX
 * ------------------
 * Unfortunately, several libraries that supposedly conform to
 * the ANSI standard do not define RAND_MAX in <stdlib.h>.  To
 * reduce portability problems, this interface defines RAND_MAX
 * to be the largest positive integer if it is undefined.
 */
#ifndef RAND_MAX
#define RAND_MAX ((int) ((unsigned) ~0 >> 1))
#endif

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

double RandomReal(double low, double high);
MatrixObject *c_matrix_allocate(int rows, int columns);
void c_matrix_deallocate(MatrixObject *matrix);
void c_matrix_str(MatrixObject *matrix);
MatrixObject *c_matrix_fill(int rows, int columns, double value);
MatrixObject *c_matrix_random(int rows, int columns, double min, double max);
MatrixObject *c_matrix_identity(int rows);
MatrixObject *c_matrix_add(MatrixObject *matrix1, MatrixObject *matrix2);
MatrixObject *c_matrix_mult(MatrixObject *matrix, double a);
MatrixObject *c_matrix_negative(MatrixObject *matrix);
MatrixObject *c_matrix_sub(MatrixObject *matrix1, MatrixObject *matrix2);
MatrixObject *c_matrix_transpose(MatrixObject *matrix);
MatrixObject *c_matrix_dot(MatrixObject *matrix1, MatrixObject *matrix2);
