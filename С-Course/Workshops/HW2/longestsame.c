#include <stdio.h>

int main(){

    int number, x, i, count, prev, res, index, flag;

    count = 0;
    res = 0;
    flag = 0;

    printf("Enter number of elements: ");
    scanf("%d", &number);

    for (i=0; i < number; i++){
        scanf("%d", &x);
        if (i == 0){
            prev = x;
        }
        if (x == prev && i != 0){
            count += 1;
            if (count > res){
                res = count;
            }
            if (flag == 0){
                index = i - 1;
            }
            flag = 1;
        }
        else {
            flag = 0;
            count = 1;
        }
        prev = x;
    }

    if (count > res){
        res = count;
    }

    printf("Length of the longest sequence of the same numbers is %d\n", res);
    printf("Index of the beginning %d\n", index);

    return 0;
}
