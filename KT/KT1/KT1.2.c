#include <stdio.h>
#include <math.h>

double function(double x, double a, double b){
    double y;
    y = a * pow(x, 3) - b/a * x + exp(-x);
    return y;
}

int main(){

    double a, b, x, min, temp;

    printf("Enter a: ");
    scanf("%lf", &a);

    printf("Enter b: ");
    scanf("%lf", &b);

    if (a == 0){
        printf("Zero division exception\n");
    }
    else {
        for(x=-5; x <= 1; x+=0.01){
            temp = function(x, a, b);
            if (x == -5){
                min = temp;
            }
            else if (temp < min){
                    min = temp;
            }
        }
        printf("Minimum: %lf\n", min);
    }
    return 0;
}
