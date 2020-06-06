#include <stdio.h>

int len(char *str){
    int len = 0;
    while (str[len] != '\0'){
        len += 1;
    }
    return len;
}

int count_digits(char *str){
    int count = 0;
    int i;

    for (i = 0; i < len(str); i++){
        if (str[i] == '1' || str[i] == '2' || str[i] == '3' || str[i] == '4' || str[i] == '5' ||
            str[i] == '6' || str[i] == '7' || str[i] == '8' || str[i] == '9' || str[i] == '0'){
            count += 1;
        }
    }

    return count;
}
int main()
{
    char str[40];

    scanf("%39s", str);

    printf("Number of digits in string: %d\n", count_digits(str));

    return 0;
}
