#include <stdio.h>

int main()
{
        int sum_odd, sum_even;
        int i;

        sum_odd = 0;
        sum_even = 0;

        for (i = 1; i <= 100; i += 1){
            if (i % 2 == 0){
                sum_even += i;
            }
            else sum_odd += i;
        }

        printf("Sum of even numbers from 1 to 100: %d\n", sum_even);
        printf("Sum of odd numbers from 1 to 100: %d\n", sum_odd);

        return 0;
}
