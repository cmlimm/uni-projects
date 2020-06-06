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
 * Function: c_matrix_allocate
 * -------------------------
 * allocates memory for matrix of given shape
 *
 * returns: MatrixObject
 */
MatrixObject *c_matrix_allocate(int rows, int columns){
    MatrixObject *matrix = malloc(sizeof(MatrixObject));
    matrix->values = malloc(sizeof(double *)*rows);
    int i;

    matrix->rows = rows;
    matrix->columns = columns;

    for (i = 0; i < rows; i++){
        matrix->values[i] = malloc(sizeof(double)*columns);
    }

    return matrix;
}

/*
 * Function: c_matrix_deallocate
 * ---------------------------
 * deallocates memory used by matrix
 *
 * returns: nothing
 */
void c_matrix_deallocate(MatrixObject *matrix){
    int i;

    for (i = 0; i < matrix->rows; i++){
        free(matrix->values[i]);
    }
    free(matrix->values);
    free(matrix);

}

/*
 * Function: c_matrix_show
 * ---------------------
 * prints matrix
 *
 * returns: nothing
 */
void c_matrix_str(MatrixObject *matrix){
    int i, j;

    for (i = 0; i < matrix->rows; i++){
        for (j = 0; j < matrix->columns; j++){
            printf("%lf ", matrix->values[i][j]);
        }
        printf("\n");
    }

}

/*
 * Function: c_matrix_fill
 * ---------------------
 * creates matrix filled with given values
 *
 * returns: MatrixObject
 */
MatrixObject *c_matrix_fill(int rows, int columns, double value){
    int i, j;
    MatrixObject *matrix;

    matrix = c_matrix_allocate(rows, columns);

    for (i = 0; i < matrix->rows; i++){
        for (j = 0; j < matrix->columns; j++){
            matrix->values[i][j] = value;
        }
    }

    return matrix;
}

/*
 * Function: c_matrix_random
 * -----------------------
 * creates matrix filled with random values between min and max, inclusive
 *
 * returns: MatrixObject
 */
MatrixObject *c_matrix_random(int rows, int columns, double min, double max){
    int i, j;
    MatrixObject *matrix;

    matrix = c_matrix_allocate(rows, columns);

    for (i = 0; i < matrix->rows; i++){
        for (j = 0; j < matrix->columns; j++){
            matrix->values[i][j] = RandomReal(min, max);
        }
    }

    return matrix;
}

/*
 * Function: c_matrix_identity
 * -------------------------
 * creates identity matrix
 *
 * returns: MatrixObject
 */
MatrixObject *c_matrix_identity(int rows){
    int i, j;
    MatrixObject *matrix;

    matrix = c_matrix_allocate(rows, rows);

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
 * Function: c_matrix_add
 * --------------------
 * adds two matrixes
 *
 * returns: MatrixObject
 */
MatrixObject *c_matrix_add(MatrixObject *matrix1, MatrixObject *matrix2){
    int i, j;
    int rows = matrix1->rows;
    int columns = matrix1->columns;
    MatrixObject *matrix;

    matrix = c_matrix_allocate(rows, columns);

    for (i = 0; i < matrix->rows; i++){
        for (j = 0; j < matrix->columns; j++){
            matrix->values[i][j] = matrix1->values[i][j] + matrix2->values[i][j];
        }
    }

    return matrix;
}

/*
 * Function: c_matrix_mult
 * ---------------------
 * multiplies matrix by a number
 *
 * returns: MatrixObject
 */
MatrixObject *c_matrix_mult(MatrixObject *matrix, double a){
    int i, j;
    int rows = matrix->rows;
    int columns = matrix->columns;
    MatrixObject *c_matrix_result;

    c_matrix_result = c_matrix_allocate(rows, columns);

    for (i = 0; i < matrix->rows; i++){
        for (j = 0; j < matrix->columns; j++){
            c_matrix_result->values[i][j] = matrix->values[i][j]*a;
        }
    }

    return c_matrix_result;
}

/*
 * Function: c_matrix_negative
 * -------------------------
 * multiplies matrix by -1
 *
 * returns: MatrixObject
 */
MatrixObject *c_matrix_negative(MatrixObject *matrix){
    return c_matrix_mult(matrix, -1);
}

/*
 * Function: c_matrix_sub
 * --------------------
 * subtracts two matrixes
 *
 * returns: MatrixObject
 */
MatrixObject *c_matrix_sub(MatrixObject *matrix1, MatrixObject *matrix2){
    return c_matrix_add(matrix1, c_matrix_negative(matrix2));
}

/*
 * Function: c_matrix_transpose
 * --------------------------
 * transposes matrix
 *
 * returns: MatrixObject
 */
MatrixObject *c_matrix_transpose(MatrixObject *matrix){
    int i, j;
    int rows = matrix->rows;
    int columns = matrix->columns;
    MatrixObject *c_matrix_result;

    c_matrix_result = c_matrix_allocate(columns, rows);

    for (i = 0; i < matrix->columns; i++){
        for (j = 0; j < matrix->rows; j++){
            c_matrix_result->values[i][j] = matrix->values[j][i];
        }
    }

    return c_matrix_result;
}

/*
 * Function: c_matrix_dot
 * --------------------
 * multiplies matrix by matrix
 * only works if number of columns of matrix1 equals
 * number of rows of matrix2
 *
 * returns: MatrixObject
 */
MatrixObject *c_matrix_dot(MatrixObject *matrix1, MatrixObject *matrix2){
    int i, j, k;
    int rows = matrix1->rows;
    int columns = matrix2->columns;
    int length = matrix1->columns;
    double vector_dot;
    MatrixObject *c_matrix_result;

    c_matrix_result = c_matrix_allocate(rows, columns);

    for (i = 0; i < rows; i++){
        for (j = 0; j < columns; j++){
            vector_dot = 0;
            for (k = 0; k < length; k++){
                vector_dot += matrix1->values[i][k]*matrix2->values[k][j];
            }
            c_matrix_result->values[i][j] = vector_dot;
        }
    }

    return c_matrix_result;
}

int main(){
    int rows, columns;
    MatrixObject *matrix;
    MatrixObject *matrix1;
    MatrixObject *matrix2;

    rows = 2;
    columns = 3;

    /*matrix1 = c_matrix_allocate(columns, columns);*/
    /*matrix2 = c_matrix_allocate(columns, columns);*/
    /*matrix1 = c_matrix_allocate(rows, columns);*/
    /*matrix2 = c_matrix_allocate(rows, columns);*/
    matrix1 = c_matrix_allocate(columns, rows);
    matrix2 = c_matrix_allocate(rows, columns);

    /*matrix1->values[0][0] = 1; matrix1->values[0][1] = 2; matrix1->values[0][2] = 3;
    matrix1->values[1][0] = 4; matrix1->values[1][1] = 5; matrix1->values[1][2] = 6;
    matrix1->values[2][0] = 7; matrix1->values[2][1] = 8; matrix1->values[2][2] = 9;*/

    /*matrix2->values[0][0] = 1; matrix2->values[0][1] = 2; matrix2->values[0][2] = 3;
    matrix2->values[1][0] = 4; matrix2->values[1][1] = 5; matrix2->values[1][2] = 6;
    matrix2->values[2][0] = 7; matrix2->values[2][1] = 8; matrix2->values[2][2] = 9;*/
    /*matrix1->values[0][0] = 1; matrix1->values[0][1] = 2; matrix1->values[0][2] = 3;
    matrix1->values[1][0] = 4; matrix1->values[1][1] = 5; matrix1->values[1][2] = 6;*/

    matrix1->values[0][0] = 1; matrix1->values[0][1] = 2;
    matrix1->values[1][0] = 3; matrix1->values[1][1] = 4;
    matrix1->values[2][0] = 5; matrix1->values[2][1] = 6;

    matrix2->values[0][0] = 7; matrix2->values[0][1] = 8; matrix2->values[0][2] = 9;
    matrix2->values[1][0] = 10; matrix2->values[1][1] = 11; matrix2->values[1][2] = 12;

    printf("Filling matrix...\n");
    /*matrix = c_matrix_fill(rows, columns, 1.0);*/
    /*matrix = c_matrix_random(rows, columns, 1.5, 2.5);*/
    /*matrix = c_matrix_identity(rows);*/
    /*matrix = c_matrix_add(matrix1, matrix2);*/
    /*matrix = c_matrix_mult(matrix1, 2.1);*/
    /*matrix = c_matrix_negative(matrix1);*/
    /*matrix = c_matrix_sub(matrix1, matrix2);*/
    /*matrix = c_matrix_transpose(matrix1);*/
    matrix = c_matrix_dot(matrix1, matrix2);
    printf("Showing matrix...\n");
    c_matrix_str(matrix);
    printf("Deallocating memory...\n");
    c_matrix_deallocate(matrix);

    return 0;
}
