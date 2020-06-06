#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 10

int main()
{
    int a[] = {1, 1, 1, 1, 2, 2, 2, 3, 10, 6};
    int i, flag;
    srand(time(NULL));

    for(i = 0; i < N; i++){
        printf("%d ", a[i]);
    }
    printf("\n");

    flag = 0;

    for(i = 0; i < N; i++){
        if (i != 0 && a[i] < a[i-1]){
            flag = 1;
        }
    }

    if (flag == 0){
        printf("Array is increasing\n");
    }
    else {
        printf("Array is not increasing\n");
    }

    return 0;
}
