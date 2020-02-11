#include <stdio.h>

long int factorial(int number, long int result)
{
    if (number == 1)
    {
        return result;
    }
    else return factorial(number - 1, result*number);
}

int main()
{
   int number;

   number = 0;

   printf("Введите число: ");
   scanf("%d", &number);

   printf("Факториал числа %d: %ld\n", number, factorial(number, 1));

   return 0;   /* indicate program ended successfully */
}
