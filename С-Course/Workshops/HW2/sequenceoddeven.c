#include <stdio.h>

int main(){

    int number, x, i, count_even, count_odd;

    count_even = 0;
    count_odd = 0;

    printf("Enter number of elements: ");
    scanf("%d", &number);

    for (i=0; i < number; i++){
        scanf("%d", &x);
        if (x % 2 == 0){
            count_even += 1;
            if (count_odd != 0){
                printf("Odd sequence length: %d\n", count_odd);
                count_odd = 0;
            }
        }
        else {
            count_odd += 1;
            if (count_even != 0){
                printf("Even sequence length: %d\n", count_even);
                count_even = 0;
            }
        }
    }

    if (count_even != 0){
        printf("Even sequence length: %d\n", count_even);
    }

    if (count_odd != 0){
        printf("Odd sequence length: %d\n", count_odd);
    }

    return 0;
}
