#include <stdio.h>

int iscube(int x)
{
    int temp = 1;

    while (temp <= x){
        if (temp*temp*temp == x){
            return 0;
        }
        else temp += 1;
    }

    return 1;
}

int main()
{
        int number;
        int res;

        printf("Введите число: ");
        scanf("%d", &number);

        res = iscube(number);

        if (res == 1){
            printf("Это не куб\n");
        }
        else printf("Это куб\n");

        return 0;
}
