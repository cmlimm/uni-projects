#include <stdio.h>

int main()
{
        int sum;
        int i;

        sum = 0;

        for (i = 2; i <= 30; i += 2){
            sum += i;
        }

        printf("Sum of even numbers from 2 to 30: %d\n", sum);

        return 0;
}
