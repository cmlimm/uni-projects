#include <stdio.h>
#include <math.h>

void squares(int n)
{
    int i;
    int prev, prev_square;

    prev = 1;
    prev_square = 1;

    for (i=1; i<=n; i++){
        printf("%d\n", prev_square);
        prev_square = prev_square + prev + prev + 1;
        prev += 1;
    }
}

int main(){
    int n;

    printf("Enter n: ");
    scanf("%d", &n);

    squares(n);

    return 0;
}
