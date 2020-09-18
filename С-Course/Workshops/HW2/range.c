#include <stdio.h>

int main(){

    int start, step, stop, count, sum;

    sum = 0;
    count = 0;

    printf("Enter start: ");
    scanf("%d", &start);

    printf("Enter step: ");
    scanf("%d", &step);

    printf("Enter stop: ");
    scanf("%d", &stop);

    while (start <= stop){
        sum += start;
        count += 1;
        start += step;
    }

    printf("Sum: %d\n", sum);
    printf("Number of elements: %d\n", count);
    return 0;
}
