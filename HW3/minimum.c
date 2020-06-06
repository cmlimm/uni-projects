#include <stdio.h>
#include <math.h>

double min(double x, double y, double z)
{
    if (x < y){
        if (x < z){
            return x;
        }
    }
    if (y < x){
        if (y < z){
            return y;
        }
    }

    return z;
}

int main()
{
        double x, y, z;
        double res;

        printf("Enter numbers: ");
        scanf("%lf %lf %lf", &x, &y, &z);

        res = min(x, y, z);

        printf("Minimum is %f\n", res);

        return 0;
}
