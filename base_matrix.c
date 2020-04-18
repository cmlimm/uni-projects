#include "base_matrix.h"
#include <stdio.h>
#include <stdlib.h>

/*
 * Function: matrix_allocate
 * -------------------------
 * allocates memory for matrix of given shape
 * rows: integer number of rows
 * columns: integer number of columns
 *
 * returns: matrix
 */
MatrixObject *matrix_allocate(int rows, int columns){
    MatrixObject *matrix = malloc(sizeof(MatrixObject));
    matrix->values = malloc(sizeof(double *)*rows);
    size_t i;

    matrix->rows = rows;
    matrix->columns = columns;

    for (i = 0; i < rows; i++){
        matrix->values[i] = malloc(sizeof(double)*columns);
    }

    return matrix;
}

/*
 * Function: matrix_deallocate
 * ---------------------------
 * deallocates memory used by matrix
 *
 * returns: nothing
 */
void matrix_deallocate(MatrixObject *matrix){
    size_t i;

    for (i = 0; i < matrix->rows; i++){
        free(matrix->values[i]);
    }
    free(matrix->values);
    free(matrix);

}

/*
 * Function: matrix_create
 * -----------------------
 * fills matrix with given values
 * matrix: matrix to fill
 * value: value to fill matrix with
 *
 * returns: nothing
 */
MatrixObject *matrix_fill(int rows, int columns, double value){
    int i, j;
    MatrixObject *matrix;

    matrix = matrix_allocate(rows, columns);

    for (i = 0; i < matrix->rows; i++){
        for (j = 0; j < matrix->columns; j++){
            matrix->values[i][j] = value;
        }
    }

    return matrix;
}

/*
 * Function: matrix_show
 * ---------------------
 * prints matrix
 * matrix: matrix to print
 *
 * returns: nothing
 */
void matrix_show(MatrixObject *matrix){
    int i, j;

    for (i = 0; i < matrix->rows; i++){
        for (j = 0; j < matrix->columns; j++){
            printf("%lf ", matrix->values[i][j]);
        }
        printf("\n");
    }

}

int main(){
    int rows, columns, value;
    MatrixObject *matrix;

    rows = 3;
    columns = 4;
    value = 1;

    printf("Filling matrix...\n");
    matrix = matrix_fill(rows, columns, value);
    printf("Showing matrix...\n");
    matrix_show(matrix);
    printf("Deallocating memory...\n");
    matrix_deallocate(matrix);

    return 0;
}
