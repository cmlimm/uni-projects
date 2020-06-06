#include <stdio.h>

long int factorial(int number, long int result)
{
    if (number == 1)
    {
        printf("Reached the end of recursion, current result: %ld\n", result);
        return result;
    }
    else{
        printf("Next factor: %d, current result: %ld\n", number, result);
        return factorial(number - 1, result*number);
    }
}

int main()
{
   int number;

   number = 0;

   printf("Enter number: ");
   scanf("%d", &number);

   printf("Factorial of number %d: %ld\n", number, factorial(number, 1));

   return 0;
}
