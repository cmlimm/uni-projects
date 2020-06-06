#include <stdio.h>

int reverse(int n)
{
    int res = 0;

    while (n != 0){
        res *= 10;
        res += n % 10;
        n = n / 10;
    }

    return res;
}

int dec_to_bin(int n){

    int i, k;
    int res = 0;
    int factor = 1;
    int help = 1;

    for (i = 0; i <= 31; i++)
    {
      k = n >> i;

      if (k & 1) {
          res += 1*factor*help;
          factor *= 10;
          help = 1;
      }
      else {
          help *= 10;
      }
    }

    return res;
}

int main()
{
    int n, res;

    printf("Enter n: ");
    scanf("%d", &n);

    res = dec_to_bin(n);

    printf("%d in binary number system is: %d\n", n, res);

    if (res == reverse(res)){
        printf("It is symmetric\n");
    } else printf("It is not symmetric\n");

    return 0;
}
