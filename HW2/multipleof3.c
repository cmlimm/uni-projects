#include <stdio.h>

int main()
{
        int i;
        
        printf("Все двузначные положительные числа, кратные 3\n");

        for (i = 12; i <= 99; i += 3){
            printf("%d\n", i);
        }

        return 0;
}
