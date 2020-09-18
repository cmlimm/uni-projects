#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 10

int main()
{
    int a[N];
    int i;
    srand(time(NULL));

    for(i = 0; i < N; i++){
        a[i] = rand()%100;
        printf("%d ", a[i]);
    }
    printf("\n");

    printf("Odd index: ");
    for(i = 0; i < N; i+=2){
        printf("%d ", a[i]);
    }
    printf("\n");

    printf("Even index: ");
    for(i = 1; i < N; i+=2){
        printf("%d ", a[i]);
    }
    printf("\n");

    return 0;
}
