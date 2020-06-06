#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 10

int main()
{
    int a[N];
    int i;
    int sum = 0;
    double avg;
    srand(time(NULL));

    for(i = 0; i < N; i++){
        a[i] = rand()%100;
        printf("%d ", a[i]);
    }
    printf("\n");

    for(i = 0; i < N; i++){
        sum += a[i];
    }

    avg = (double) sum / N;
    printf("Average of elements: %lf\n", avg);

    return 0;
}
