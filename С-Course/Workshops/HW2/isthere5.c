#include <stdio.h>

int is_there_5(int n){
    int digit, dummy;
    dummy = n;
    while (dummy != 0){
        digit = dummy % 10;
        dummy = dummy / 10;
        if (digit == 5){
            return 1;
        }
    }
    return 0;
}

int main()
{
   int number, res;

   printf("Введите число: ");
   scanf("%d", &number);

   res = is_there_5(number);

   if (res == 0){
       printf("В числе %d нет пятерки\n", number);
   } else printf("В числе %d есть пятерка\n", number);
   return 0;
}
