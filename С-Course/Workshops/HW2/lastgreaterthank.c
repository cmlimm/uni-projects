#include <stdio.h>

int main(){

    int number, x, k, i, index;

    printf("Enter number of elements: ");
    scanf("%d", &number);

    printf("Enter k: ");
    scanf("%d", &k);

    for (i=0; i < number; i++){
        scanf("%d", &x);
        if (x > k){
            index = i;
        }
    }

    printf("Index of the last number greater than %d is %d\n", k, index);
    return 0;
}
