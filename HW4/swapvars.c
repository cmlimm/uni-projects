#include <stdio.h>
void swap(int *a, int *b){
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

int main()
{
    int x;
    int y;

    x = 1;
    y = 5;

    swap(&x, &y);
    printf("x - %d, y - %d\n", x, y);
    return 0;
}
