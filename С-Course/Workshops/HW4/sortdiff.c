#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 10

int main()
{
    int a[] = {5, 4, 3, 2, 1, 1, 2, 3, 4, 5};
    int size_a = sizeof(a)/sizeof(int);
    int b[size_a];
    int i, j, count, temp;
    srand(time(NULL));

    for(i = 0; i < size_a; i++){
        printf("%d ", a[i]);
    }
    printf("\n");

    for(i = 0; i < size_a; i++){
        for(j = i+1; j < size_a; j++){
            if(a[i]>a[j]){
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }

    count = 0;
    for(i = 0; i < size_a; i++){
        if (a[i] != a[i - 1]){
            count += 1;
            b[count - 1] = a[i];
        }
    }

    for(i = 0; i < count; i++){
        printf("%d ", b[i]);
    }
    printf("\n");
    return 0;
}
