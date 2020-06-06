#include <stdio.h>

int count_odd_digits(int x)
{
    int res = 0;
    int count = 0;

    while (x != 0){
        res = x % 10;
        if (res % 2 == 1){
            count += 1;
        }
        x = x / 10;
    }

    return count;
}

int main()
{
        int x;
        int res;

        printf("Enter number: ");
        scanf("%d", &x);

        res = count_odd_digits(x);

        printf("Number of odd digits: %d\n", res);

        return 0;
}
