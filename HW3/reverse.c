#include <stdio.h>

int reverse(int x)
{
    int res = 0;

    while (x != 0){
        res *= 10;
        res += x % 10;
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

        res = reverse(x);

        printf("Reverse: %d\n", res);

        return 0;
}
