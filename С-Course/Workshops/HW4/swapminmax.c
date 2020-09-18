#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 10

int main()
{
    int a[N];
    int i;
    int i_min, i_max, temp;
    srand(time(NULL));

    for(i = 0; i < N; i++){
        a[i] = rand()%100;
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

    temp = a[i_min];
    a[i_min] = a[i_max];
    a[i_max] = temp;

    printf("Swapped minimum and maximum:\n");
    for(i = 0; i < N; i++){
        printf("%d ", a[i]);
    }
    printf("\n");

    return 0;
}
