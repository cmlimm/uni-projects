#include <stdio.h>
#include <math.h>

int main(){

    int number, x, i, prev, flag;

    flag = 1;

    printf("Enter number of elements: ");
    scanf("%d", &number);

    for (i=0; i < number; i++){
        scanf("%d", &x);
        if (x < prev && i != 0){
            flag = 0;
        }
        prev = x;
    }

    if (flag == 1) {
        printf("It is increasing\n");
    } else printf("It is not increasing\n");
    return 0;
}
