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
matrix *matrix_allocate(int rows, int columns){
    matrix *mtrx = malloc(sizeof(matrix));
    mtrx->values = malloc(sizeof(double *)*rows);
    size_t i;

    mtrx->rows = rows;
    mtrx->columns = columns;

    for (i = 0; i < rows; i++){
        mtrx->values[i] = malloc(sizeof(double)*columns);
    }

    return mtrx;
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
    free(mtrx);

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
    matrix *mtrx;

    rows = 3;
    columns = 4;
    value = 1;

    printf("Allocating memory...\n");
    mtrx = matrix_allocate(rows, columns);
    printf("Filling matrix...\n");
    matrix_fill(mtrx, value);
    printf("Showing matrix...\n");
    matrix_show(mtrx);
    printf("Deallocating memory...\n");
    matrix_deallocate(mtrx);

    return 0;
}
