#include <stdio.h>
#include <math.h>

int sum_of_two_squares(int n, int* add_i, int* add_j)
{
    int i, j;
    for (i=1; i*i<=n; i++){
        for(j=1; j*j<=n; j++){
            if (i*i + j*j == n){
                *add_i = i;
                *add_j = j;
                return 1;
            }
        }
    }
    return 0;
}

int main(){
    int n, i, j;
    int res;

    printf("Enter n: ");
    scanf("%d", &n);

    res = sum_of_two_squares(n, &i, &j);
    if (res == 0){
        printf("Can not be expressed as the sum of two squares\n");
    } else printf("n = %d^2 + %d^2\n", i, j);

    return 0;
}
