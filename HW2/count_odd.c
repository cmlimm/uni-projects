#include <stdio.h>

int main()
{
   int number, digit, dummy, counter;

   number = 0;
   digit = 0;
   counter = 0;

   printf("Введите число: ");
   scanf("%d", &number);

   dummy = number;

   while (dummy != 0){
       digit = dummy % 10;
       dummy = dummy / 10;
       if (digit % 2 == 1){
           counter += 1;
       }
   }

   printf("В числе %d %d нечетных цифр\n", number, counter);

   return 0;
}
