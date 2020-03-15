#include <stdio.h>

int main()
{
        int total = 0;
        int x, y, z, i;

        for(i=100; i<1000; i++){
            x = i % 10;
            y = i / 10 % 10;
            z = i / 100;
            if ((x == y) + (x == z) + (z == y) == 0){
                total += 1;
            }
        }

        printf("Количество трехзначных чисел без повторяющихся цифр: %d\n", total);

        return 0;
}
