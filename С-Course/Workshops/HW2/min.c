#include <stdio.h>

int main()
{
        int number;
        int temp;
        int min;
        int i;

        number = 0;
        min = 0;

        printf("Enter number of numbers: ");
        scanf("%d", &number);

        for (i = 0; i < number; i++){
            printf("Enter number: ");
            scanf("%d", &temp);
            if (i == 0){
                min = temp;
            }
            else if (temp < min){
                min = temp;
            }
        }

        printf("Minimum: %d\n", min);

        return 0;
}
