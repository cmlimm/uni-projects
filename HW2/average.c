#include <stdio.h>

int main()
{
        int number;
        int count;
        int sum;
        double average;

        number = 0;
        sum = 0;
        count = 0;
        average = 0;

        while (number != 9999){
            sum += number;
            count += 1;
            printf("Enter number: ");
            scanf("%d", &number);
        }

        average = (sum) / ((double)count - 1);
        printf("Average: %.2lf\n", average);

        return 0;
}
