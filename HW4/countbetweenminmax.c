#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 10

int main()
{
    int a[] = {1, 2, 3, 4, 5, 1, 2, 3, 4, 4};
    int i;
    int i_min, i_max, beg, end, sum;
    srand(time(NULL));

    for(i = 0; i < N; i++){
        printf("%d ", a[i]);
    }
    printf("\n");

    i_min = 0;
    i_max = 0;

    for(i = 0; i < N; i++){
        if (a[i] > a[i_max]){
            i_max = i;
        }
        if (a[i] < a[i_min]){
            i_min = i;
        }
    }

    if (i_max > i_min){
        beg = i_min;
        end = i_max;
    }
    else{
        beg = i_max;
        end = i_min;
    }

    sum = 0;

    for(i = beg + 1; i < end; i++){
        sum += a[i];
    }

    printf("Sum of elements between minimum and maximum: %d\n", sum);

    return 0;
}
