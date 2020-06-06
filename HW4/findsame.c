#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 10

int main()
{
    // int a[] = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1};
    // int b[] = {1, 1, 3, 4};
    // int a[] = {1, 2, 3, 4, 5, 4, 3, 2, 1};
    // int b[] = {1, 2, 3, 4, 5, 7, 3, 2, 1};
    // int a[] = {1, 2, 3, 4};
    // int b[] = {5, 6, 7, 8, 9};
    // int a[] = {1, 2, 3, 4};
    // int b[] = {1, 1, 1, 1, 1};
    int a[] = {1, 1, 1, 1};
    int b[] = {1, 1, 1, 1, 1};
    int i, j, k, t, count, marker;
    srand(time(NULL));

    int size_a = sizeof(a)/sizeof(int);
    int size_b = sizeof(b)/sizeof(int);

    for(i = 0; i < size_a; i++){
        printf("%d ", a[i]);
    }
    printf("\n");

    for(j = 0; j < size_b; j++){
        printf("%d ", b[j]);
    }
    printf("\n");

    marker = a[0];
    count = 0;
    for (i = 0; i < size_a; i++){
        if (i != 0 && a[i] == marker){
            continue;
        }
        else{
            for (j = 0; j < size_b; j++){
                if (a[i] == b[j]){
                    count += 1;
                    break;
                }
            }
            for (k = i + 1; k < size_a; k++){
                if (a[i] == a[k]){
                    a[k] = marker;
                }
            }
            a[i] = marker;
        }
    }

    printf("Number of common different elements of arrays: %d\n", count);
    return 0;
}
