#include <stdio.h>

int gcd(int x, int y)
{
    int temp = 0;

    while (x != y){
        if (x > y){
            temp = x;
            x = y;
            y = temp;
        }
        y = y - x;
    }

    return x;
}

int main()
{
        int x, y;
        int res;

        printf("Enter first number: ");
        scanf("%d", &x);

        printf("Enter second number: ");
        scanf("%d", &y);

        res = gcd(x, y);

        printf("GCD: %d\n", res);

        return 0;
}
