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
    int i;

    for (i = 1; i <= 5; i++){
        printf("%d | %ld\n", i, factorial(i, 1));
    }

    return 0;
}
