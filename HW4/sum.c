#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 10

int main()
{
    int a[N];
    int i;
    int sum = 0;
    srand(time(NULL));

    for(i = 0; i < N; i++){
        a[i] = rand()%100;
        printf("%d ", a[i]);
    }
    printf("\n");

    for(i = 0; i < N; i++){
        sum += a[i];
    }

    printf("Sum of elements: %d\n", sum);

    return 0;
}
