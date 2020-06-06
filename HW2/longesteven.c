#include <stdio.h>

int main(){

    int number, x, i, count_even, count_odd, res;

    count_even = 0;
    count_odd = 0;
    res = 0;

    printf("Enter number of elements: ");
    scanf("%d", &number);

    for (i=0; i < number; i++){
        scanf("%d", &x);
        if (x % 2 == 0){
            count_even += 1;
            if (count_even > res){
                res = count_even;
            }
        }
        else {
            count_even = 0;
        }
    }

    if (count_even > res){
        res = count_even;
    }

    printf("Length of the longest sequence of even numbers is %d\n", res);

    return 0;
}
