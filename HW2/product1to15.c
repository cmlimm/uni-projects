#include <stdio.h>

int main()
{
        int product;
        int i;

        product = 1;

        for (i = 1; i <= 15; i += 2){
            product *= i;
        }

        printf("Product of odd numbers from 1 to 15: %d\n", product);

        return 0;
}
