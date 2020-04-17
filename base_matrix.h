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

void matrix_allocate(matrix *mtrx, int rows, int columns);
void matrix_deallocate(matrix *mtrx);
void matrix_fill(matrix *mtrx, double value);
matrix matrix_row(int index);
matrix matrix_column(int index);
void matrix_show(matrix *mtrx);
