#include <stdio.h>
#include <math.h>

void prime_factors(int n)
{
    int i;
    int count = 0;

    while (n % 2 == 0){
        printf("%d ", 2);
        n = n / 2;
        count = 1;
    }
    if (count != 0){
        printf("\n");
        count = 0;
    }

    for (i=3; i <= sqrt(n); i += 2){

        while (n % i == 0){
            printf("%d ", i);
            n = n / i;
            count = 1;
        }
        if (count != 0){
            printf("\n");
            count = 0;
        }
    }

    if (n > 2){
        printf("%d\n", n);
    }

}

int main(){
    int n;

    printf("Enter n: ");
    scanf("%d", &n);

    prime_factors(n);

    return 0;
}
