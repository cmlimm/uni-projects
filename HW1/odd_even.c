#include <stdio.h>

int main()
{
   int number;
   /* initialization phase */
   number = 0;

   printf("Введите число: ");
   scanf("%d", &number);

   if (number % 2 == 0){
       printf("Число %d - четное\n", number);
   }
   else printf("Число %d - нечетное\n", number);

   return 0;   /* indicate program ended successfully */
}
