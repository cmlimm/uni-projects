#include <stdio.h>

int ispower3(int x)
{
    int temp = 1;

    while (temp <= x){
        if (temp == x){
            return 0;
        }
        else temp *= 3;
    }

    return 1;
}

int main()
{
        int number;
        int res;

        printf("Введите число: ");
        scanf("%d", &number);

        res = ispower3(number);

        if (res == 1){
            printf("Это не степень тройки\n");
        }
        else printf("Это степень тройки\n");

        return 0;
}
