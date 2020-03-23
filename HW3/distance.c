#include <stdio.h>
#include <math.h>

double distance(x_1, y_1, x_2, y_2)
{
    double dist;

    dist = sqrt(pow(x_2 - x_1, 2) + pow(y_2 - y_1, 2));

    return dist;
}

int main()
{
        double x_1, x_2, y_1, y_2;
        double dist;

        printf("Enter coordinates of the first point: ");
        scanf("%lf %lf", &x_1, &y_1);

        printf("Enter coordinates of the first point: ");
        scanf("%lf %lf", &x_2, &y_2);

        dist = distance(x_1, y_1, x_2, y_2);

        printf("Distance: %.2lf\n", dist);

        return 0;
}
