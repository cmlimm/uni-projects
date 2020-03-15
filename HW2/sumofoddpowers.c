#include <stdio.h>

long int factorial(int number, long int result)
{
    if (number == 1)
    {
        return result;
    }
    else return factorial(number - 1, result*number);
}

double sum_of_odd_powers(double x, int n)
{
    double sum = 0;
    double factor = x;
    int i;

    for (i=1; i<=2*n+1; i+=2){
        sum += factor/factorial(i, 1);
        factor *= -1*x*x;
    }

    return sum;
}

int main()
{
        double x;
        double res;
        int n;

        printf("Enter number x: ");
        scanf("%lf", &x);

        printf("Enter n: ");
        scanf("%d", &n);

        res = sum_of_odd_powers(x, n);
        printf("x/1! - x^3/3! + x^5/5! - ... + (-1)^(n)x^(2n+1)/(2n+1)! = %lf\n", res);

        return 0;
}
