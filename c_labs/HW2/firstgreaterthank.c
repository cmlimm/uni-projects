#include <stdio.h>

int main(){

    int number, x, k, i, index, flag;

    flag = 0;

    printf("Enter number of elements: ");
    scanf("%d", &number);

    printf("Enter k: ");
    scanf("%d", &k);

    for (i=0; i < number; i++){
        scanf("%d", &x);
        if (x > k && flag == 0){
            index = i;
            flag = 1;
        }
    }

    printf("Index of the first number greater than %d is %d\n", k, index);
    return 0;
}
