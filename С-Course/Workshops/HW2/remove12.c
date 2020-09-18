#include <stdio.h>

int remove12(int x)
{
    int digit = 0;
    int res = 0;
    int factor = 1;

    while (x != 0){
        digit = x % 10;
        if (digit != 1 && digit != 2){
            res += digit*factor;
            factor *= 10;
        }
        x = x / 10;
    }

    return res;
}

int main()
{
        int x;
        int res;

        printf("Enter number: ");
        scanf("%d", &x);

        res = remove12(x);
        if (res != 0){
            printf("Number with no 1's and 2's: %d\n", res);
        } else printf("Number consists only of the 1's and 2's\n");

        return 0;
}
