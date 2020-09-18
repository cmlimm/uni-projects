#include <stdio.h>

int fibonacci(int n){
    int first = 0;
    int second = 1;
    int temp;
    int i;

    for (i=3; i<=n; i++){
        temp = second;
        second += first;
        first = temp;
    }

    return second;
}

int main(){
    int n;
    int res;

    printf("Enter n greater than 2: ");
    scanf("%d", &n);

    res = fibonacci(n);

    printf("nth fibonacci number: %d\n", res);

    return 0;
}
