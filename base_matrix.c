#include "base_matrix.h"
#include <stdio.h>
#include <stdlib.h>

/*
 * Function: RandomReal
 * --------------------
 * This function come from Eric Roberts' "The Art and Science of C".
 * This function returns a random real number between
 * low and high, inclusive.
 */
double RandomReal(double low, double high)
{
  double d;

  d = (double) rand() / ((double) RAND_MAX + 1);
  return (low + d * (high - low));
}

/*
 * Function: matrix_allocate
 * -------------------------
 * allocates memory for matrix of given shape
 *
 * returns: MatrixObject
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
 * Function: matrix_show
 * ---------------------
 * prints matrix
 *
 * returns: nothing
 */
void matrix_str(MatrixObject *matrix){
    int i, j;

    for (i = 0; i < matrix->rows; i++){
        for (j = 0; j < matrix->columns; j++){
            printf("%lf ", matrix->values[i][j]);
        }
        printf("\n");
    }

}

/*
 * Function: matrix_fill
 * -----------------------
 * creates matrix filled with given values
 *
 * returns: MatrixObject
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
 * Function: matrix_random
 * -----------------------
 * creates matrix filled with random values between min and max, inclusive
 *
 * returns: MatrixObject
 */
MatrixObject *matrix_random(int rows, int columns, double min, double max){
    int i, j;
    MatrixObject *matrix;

    matrix = matrix_allocate(rows, columns);

    for (i = 0; i < matrix->rows; i++){
        for (j = 0; j < matrix->columns; j++){
            matrix->values[i][j] = RandomReal(min, max);
        }
    }

    return matrix;
}

/*
 * Function: matrix_identity
 * -----------------------
 * creates identity matrix
 *
 * returns: MatrixObject
 */
MatrixObject *matrix_identity(int rows){
    int i, j;
    MatrixObject *matrix;

    matrix = matrix_allocate(rows, rows);

    for (i = 0; i < matrix->rows; i++){
        for (j = 0; j < matrix->columns; j++){
            if (i == j)
                matrix->values[i][j] = 1.0;
            else
                matrix->values[i][j] = 0.0;
        }
    }

    return matrix;
}

/*
 * Function: matrix_add
 * -----------------------
 * adds two matrixes
 *
 * returns: MatrixObject
 */
MatrixObject *matrix_add(MatrixObject *matrix1, MatrixObject *matrix2){
    int i, j;
    int rows = matrix1->rows;
    int columns = matrix1->columns;
    MatrixObject *matrix;

    matrix = matrix_allocate(rows, columns);

    for (i = 0; i < matrix->rows; i++){
        for (j = 0; j < matrix->columns; j++){
            matrix->values[i][j] = matrix1->values[i][j] + matrix2->values[i][j];
        }
    }

    return matrix;
}

int main(){
    int rows, columns;
    MatrixObject *matrix;
    MatrixObject *matrix1, *matrix2;

    rows = 2;
    columns = 3;

    matrix1 = matrix_allocate(rows, columns);
    matrix2 = matrix_allocate(rows, columns);

    matrix1->values[0][0] = 1; matrix1->values[0][1] = 2; matrix1->values[0][2] = 3;
    matrix1->values[1][0] = 4; matrix1->values[1][1] = 5; matrix1->values[1][2] = 6;

    matrix2->values[0][0] = 7; matrix2->values[0][1] = 8; matrix2->values[0][2] = 9;
    matrix2->values[1][0] = 10; matrix2->values[1][1] = 11; matrix2->values[1][2] = 12;

    printf("Filling matrix...\n");
    /*matrix = matrix_fill(rows, columns, 1.0);*/
    /*matrix = matrix_random(rows, columns, 1.5, 2.5);*/
    /*matrix = matrix_identity(rows);*/
    matrix = matrix_add(matrix1, matrix2);
    printf("Showing matrix...\n");
    matrix_str(matrix);
    printf("Deallocating memory...\n");
    matrix_deallocate(matrix);

    return 0;
}
