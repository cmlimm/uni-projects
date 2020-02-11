#include <stdio.h>

int main()
{
   int total, counter;

   total = 0;
   counter = 10;

   while (counter >= 0){
       total += counter;
       counter -= 1;
   }
   printf("Сумма чисел от 1 до 10: %d\n", total);

   return 0;
}
