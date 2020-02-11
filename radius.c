#include <stdio.h>
#define pi 3.14159

double area(float radius)
{
    return pi*radius*radius;
}

double perimeter(float radius)
{
    return 2*pi*radius;
}

double diameter(float radius)
{
    return 2*radius;
}

int main()
{
   double radius;

   radius = 0;

   printf("Введите радиус: ");
   scanf("%lf", &radius);

   printf("Площадь: %.2lf\n", area(radius));
   printf("Периметр: %.2lf\n", perimeter(radius));
   printf("Диаметр: %.2lf\n", diameter(radius));

   return 0;   /* indicate program ended successfully */
}
