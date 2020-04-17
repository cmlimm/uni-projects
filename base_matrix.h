#define MAX_MATRIX_SIZE = 256;

/*
 * Struct: matrix
 * ----------------
 * rows: integer number of rows
 * columns: integer number of columns
 * values: 2-dimensional array of double values in matrix
 */
typedef struct matrix{
    int rows;
    int columns;
    double **values;
} matrix;

matrix *matrix_allocate(int rows, int columns);
void matrix_deallocate(matrix *mtrx);
void matrix_fill(matrix *mtrx, double value);
void matrix_show(matrix *mtrx);

void matrix_random(matrix *mtrx, int min, int max) /* not implemented */
void matrix_identity(matrix *mtrx) /* not implemented */
matrix *matrix_add(matrix *mtrx1, matrix *mtrx2) /* not implemented */
matrix *matrix_dot(matrix *mtrx1, matrix *mtrx2) /* not implemented */
matrix *matrix_mult(matrix *mtrx1, int a) /* not implemented */
matrix *matrix_transpose(matrix *mtrx1) /* not implemented */
matrix *matrix_row(int index); /* not implemented */
matrix *matrix_column(int index); /* not implemented */
double matrix_det(matrix *mtrx); /* not implemented */
