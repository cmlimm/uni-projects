#include <stdio.h>
#include <stdlib.h>

int len(char *str){
    int len = 0;
    while (str[len] != '\0'){
        len += 1;
    }
    return len;
}

char *str_chr(char *str, char c){
    int n = len(str);
    int i;
    int flag = 0;
    char *p;

    for (i = 0; i < n; i++){
        if (str[i] == c){
            p = &str[i];
            flag = 1;
            break;
        }
    }

    if (flag == 1){
        return p;
    }
    else return NULL;
}
int main()
{
    char str[40];
    char c;

    scanf("%39s", str);
    scanf(" %c", &c);

    printf("Address of char in string: %p\n", str_chr(str, c));
    return 0;
}
