#include <stdio.h>
#include <math.h>

int is_prime(int x)
{
    int temp = 2;

    if (x == 2){
        return 0;
    }

    while (temp <= sqrt(x)){
        if (x % temp == 0){
            return 1;
        }
        temp += 1;
    }

    return 0;
}

int main()
{
        int x;
        int res;

        printf("Enter number: ");
        scanf("%d", &x);

        res = is_prime(x);

        if (is_prime(x) == 1){
            printf("Number is not prime.\n");
        }
        else printf("Number is prime.\n");

        return 0;
}
