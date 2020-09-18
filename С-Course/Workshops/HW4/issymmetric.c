#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 10

int main()
{
    //int a[] = {1, 1, 1, 1, 2, 2, 2, 3, 10, 6};
    int a[] = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1};
    //int a[] = {1, 2, 3, 4, 5, 4, 3, 2, 1};
    //int a[] = {1, 2, 3, 4, 5, 7, 3, 2, 1};
    int i, flag;
    srand(time(NULL));

    int n = sizeof(a)/sizeof(int);

    for(i = 0; i < n; i++){
        printf("%d ", a[i]);
    }
    printf("\n");

    flag = 1;

    for(i = 0; i < n / 2; i++){
        printf("a[i] = %d, a[n - i - 1] %d\n", a[i], a[n-i-1]);
        if (a[i] != a[n - i - 1]){
            flag = 0;
            break;
        }
    }

    if (flag == 1){
        printf("Array is symmetric\n");
    }
    else {
        printf("Array is not symmetric\n");
    }

    return 0;
}
