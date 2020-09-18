#include <stdio.h>

int reverse(int n)
{
    int res = 0;

    while (n != 0){
        res *= 10;
        res += n % 10;
        n = n / 10;
    }

    return res;
}

int first_last_same(int n){
    if (n % 10 == reverse(n) % 10){
        return 1;
    }
    return 0;
}

int main()
{
        int n;
        int res;

        printf("Enter number: ");
        scanf("%d", &n);

        res = first_last_same(n);
        if (res == 0){
            printf("First and last digits are different\n");
        } else printf("First and last digits are same\n");

        return 0;
}
