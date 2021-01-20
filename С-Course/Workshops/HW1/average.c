#include <stdio.h>

int main()
{
   double average;              /* new data type */
   int number, total;
   int i;
   /* initialization phase */
   total = 0;
   number = 0;

   for(i = 0; i < 5; i++){
      printf("Введите число: ");
      scanf("%d", &number);
      total += number;
   }

   average = (double) total / 5;
   printf("Среднее: %.2f\n", average);

   return 0;   /* indicate program ended successfully */
}
