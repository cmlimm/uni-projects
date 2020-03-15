#include <stdio.h>

double sum_of_powers(double x, int n)
{
    double sum = 0;
    double factor = 1;
    int i;

    for (i=0; i<=n; i++){
        sum += factor;
        factor *= x;
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

        printf("Enter max power n: ");
        scanf("%d", &n);

        res = sum_of_powers(x, n);
        printf("1 + x + x^2 + ... + x^n = %lf\n", res);

        return 0;
}
