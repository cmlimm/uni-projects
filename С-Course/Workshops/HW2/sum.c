#include <stdio.h>

int main()
{
        int number;
        int temp;
        int sum;
        int i;

        number = 0;
        temp = 0;
        sum = 0;

        printf("Enter number of numbers: ");
        scanf("%d", &number);

        for (i = 0; i < number; i++){
            printf("Enter number: ");
            scanf("%d", &temp);
            sum += temp;
        }

        printf("Total: %d\n", sum);

        return 0;
}
