#include <stdio.h>

int samllestsquare(int x)
{
    int i = 1;

    while (i*i < x){
        i += 1;
    }

    return i;
}

int main()
{
        int number;
        int res;

        printf("Введите число: ");
        scanf("%d", &number);

        res = samllestsquare(number);

        printf("Ближайший наименьший квадрат задается числом: %d\n", res);

        return 0;
}
