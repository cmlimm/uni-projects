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
void matrix_allocate(matrix *mtrx, int rows, int columns){
    mtrx->values = (double **)malloc(sizeof(double *) * rows);
    size_t i;

    for (i = 0; i < rows; i++){
        mtrx->values[i] = (double *)malloc(sizeof(double) * columns);
    }

}

/*
 * Function: matrix_deallocate
 * ---------------------------
 * deallocates memory used by matrix
 *
 * returns: nothing
 */
void matrix_deallocate(matrix *mtrx){
    size_t i;

    for (i = 0; i < mtrx->rows; i++){
        free(mtrx->values[i]);
    }
    free(mtrx->values);

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
void matrix_fill(matrix *mtrx, double value){
    int i, j;

    for (i = 0; i < mtrx->rows; i++){
        for (j = 0; j < mtrx->columns; j++){
            mtrx->values[i][j] = value;
        }
    }

}

/*
 * Function: matrix_show
 * ---------------------
 * prints matrix
 * matrix: matrix to print
 *
 * returns: nothing
 */
void matrix_show(matrix *mtrx){
    int i, j;

    for (i = 0; i < mtrx->rows; i++){
        for (j = 0; j < mtrx->columns; j++){
            printf("%lf ", mtrx->values[i][j]);
        }
        printf("\n");
    }

}

int main(){
    int rows, columns, value;
    matrix *mtrx = NULL;

    rows = 3;
    columns = 4;
    value = 1;

    printf("Allocating memory...");
    matrix_allocate(mtrx, rows, columns);
    printf("Filling matrix...");
    matrix_fill(mtrx, value);
    printf("Showing memory...");
    matrix_show(mtrx);
    printf("Deallocating memory...");
    matrix_deallocate(mtrx);

    return 0;
}
