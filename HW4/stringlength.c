#include <stdio.h>

int len(char *str){
    int len = 0;
    while (str[len] != '\0'){
        len += 1;
    }
    return len;
}

int main()
{
    char str[40];

    scanf("%39s", str);

    printf("%s\n", str);
    printf("Length of string: %d\n", len(str));

    return 0;
}
