#define MAX_MATRIX_SIZE = 256;

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

MatrixObject *matrix_allocate(int rows, int columns);
void matrix_deallocate(MatrixObject *matrix);
void matrix_str(MatrixObject *matrix);
MatrixObject *matrix_fill(int rows, int columns, double value);
MatrixObject *matrix_random(int rows, int columns, double min, double max);
MatrixObject *matrix_identity(int rows);
MatrixObject *matrix_add(MatrixObject *matrix1, MatrixObject *matrix2);
MatrixObject *matrix_mult(MatrixObject *matrix, double a);
MatrixObject *matrix_negative(MatrixObject *matrix);
MatrixObject *matrix_sub(MatrixObject *matrix1, MatrixObject *matrix2);
MatrixObject *matrix_transpose(MatrixObject *matrix);

MatrixObject *matrix_dot(MatrixObject *matrix1, MatrixObject *matrix2); /* not implemented */
double matrix_det(MatrixObject *matrix); /* not implemented */
