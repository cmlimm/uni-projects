#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 10

int main()
{
    int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
    int i;
    srand(time(NULL));
    int flag = 1;

    for(i = 0; i < N; i++){
        //a[i] = rand()%100;
        printf("%d ", a[i]);
    }
    printf("\n");

    for(i = 0; i < N; i++){
        if (i != 0){
            if ((a[i] - a[i - 1]) % 2 == 0){
                flag = 0;
                break;
            }
        }
    }

    if (flag == 1){
        printf("Even and odd numbers do alternate.\n");
    }
    else {
        printf("Even and odd numbers do not alternate.\n");
    }

    return 0;
}
