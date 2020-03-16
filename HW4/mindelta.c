#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#define N 10

int main()
{
    int a[N];
    int i, i_min_delta;
    double r, min_delta, delta;
    srand(time(NULL));

    printf("Enter r: ");
    scanf("%lf", &r);

    for(i = 0; i < N; i++){
        a[i] = rand()%100;
        printf("%d ", a[i]);
    }
    printf("\n");

    min_delta = fabs(a[0] - r);
    i_min_delta = 0;

    for(i = 0; i < N; i++){
        delta = fabs(a[i] - r);
        if (delta < min_delta){
            min_delta = delta;
            i_min_delta = i;
        }
    }

    printf("Element closest to %lf is %d with index %d\n", r, a[i_min_delta], i_min_delta);
    printf("Minimal delta is %lf\n", min_delta);

    return 0;
}
