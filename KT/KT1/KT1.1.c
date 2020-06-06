#include <stdio.h>
#include <math.h>

double function(double x, double a, double b){
    double y;
    y = a * pow(x, 3) - b/a * x + exp(-x);
    return y;
}

int main(){

    double a, b, x;

    printf("Enter a: ");
    scanf("%lf", &a);

    printf("Enter b: ");
    scanf("%lf", &b);

    printf("Enter x: ");
    scanf("%lf", &x);

    if (a == 0){
        printf("Zero division exception\n");
    }
    else {
        printf("Result: %lf\n", function(x, a, b));
    }
    return 0;
}
