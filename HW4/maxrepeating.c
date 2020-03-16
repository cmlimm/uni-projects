#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 10

int main()
{
    int a[] = {1, 1, 1, 1, 2, 2, 2, 3, 5, 6};
    int i, j, current, count, max_count;
    srand(time(NULL));

    for(i = 0; i < N; i++){
        printf("%d ", a[i]);
    }
    printf("\n");

    count = 0;
    max_count = 0;

    for(i = 0; i < N; i++){
        current = a[i];
        for(j = 0; j < N; j++){
            if (a[j] == current){
                count += 1;
            }
        }
        if (count > max_count){
            max_count = count;
        }
        count = 0;
    }

    printf("Количество наиболее повторяющихся чисел: %d\n", max_count);

    return 0;
}
