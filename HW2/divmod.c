#include <stdio.h>

void find_div_mod(int n, int k, int* add_div, int* add_mod)
{
    *add_div = 0;
    *add_mod = n;

    while (n >= 0){
        n -= k;
        if (n >= 0){
            *add_div += 1;
            *add_mod = n;
        }
    }
}

int main(){
    int n, k, div, mod;

    printf("Enter n and k: ");
    scanf("%d %d", &n, &k);

    find_div_mod(n, k, &div, &mod);

    printf("n div k = %d\nn mod k = %d\n", div, mod);

    return 0;
}
