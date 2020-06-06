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
        if (min == 0 && temp > 0){
            min = temp;
        }
        if (temp < min && temp > 0){
            min = temp;
        }
    }

    if (min > 0){
        printf("Minimal positive number: %d\n", min);
    } else printf("No positive numbers\n");

    return 0;
}
