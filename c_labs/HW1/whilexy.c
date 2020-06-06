#include <stdio.h>

int main()
{
   int total, x, y, counter;
   /* initialization phase */
   total = 1;
   x = 0;
   y = 0;

   printf("Введите число: ");
   scanf("%d", &x);
   printf("Введите степень: ");
   scanf("%d", &y);

   counter = y;

   while (counter > 0){
       total *= x;
       counter -= 1;
   }
   printf("%d в степени %d равно %d\n", x, y, total);

   return 0;   /* indicate program ended successfully */
}
