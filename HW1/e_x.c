#include <stdio.h>
#include <math.h>

long int factorial(int number, long int result)
{
    if (number == 1)
    {
        return result;
    }
    else return factorial(number - 1, result*number);
}

long double taylor(double x, int n)
{
    long double e;
    int i;
    e = 1;
    for (i = 1; i < n + 1; i++){
        e += pow(x, (double) i)/factorial(i, 1);
    }
    return e;
}

int main()
{
   int n;
   double x;

   n = 0;
   x = 0;

   printf("Введите степень: ");
   scanf("%lf", &x);

   printf("Введите количество членов ряда Тейлора: ");
   scanf("%d", &n);

   printf("Приближенное значение е в степени %lf: %Lf\n", x, taylor(x, n));

   return 0;
}
