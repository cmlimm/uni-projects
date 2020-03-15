#include <stdio.h>

int main()
{
   int number, first, second, fourth, fifth;

   number = 0;

   printf("Введите число: ");
   scanf("%d", &number);

   fifth = number % 10;
   fourth = number % 100 / 10;
   second = number / 1000 % 10;
   first = number / 10000;

   if (fifth == first && fourth == second){
       printf("Число %d - палиндром\n", number);
   }
   else printf("Число %d - не палиндром\n", number);

   return 0;
}
