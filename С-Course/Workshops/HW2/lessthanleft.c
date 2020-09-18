#include <stdio.h>
#include <math.h>

int main(){

    int number, x, i, prev, count;

    count = 0;

    printf("Enter number of elements: ");
    scanf("%d", &number);

    for (i=0; i < number; i++){
        scanf("%d", &x);
        if (x < prev && i != 0){
            count += 1;
        }
        prev = x;
    }

    printf("Number of elements less than thir left neigbour: %d\n", count);

    return 0;
}
