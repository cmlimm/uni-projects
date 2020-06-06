#include <stdio.h>

int main(){

    int number, x, i, count, min;

    count = 0;
    min = 0;

    printf("Enter number of elements: ");
    scanf("%d", &number);

    for (i=0; i < number; i++){
        scanf("%d", &x);
        if (i == 0){
            min = x;
        }
        if (x < min && i != 0){
            count += 1;
            min = x;
        }
    }

    printf("Length of the sequence of numbers before minimal element is %d\n", count);

    return 0;
}
