#include <stdio.h>
#include <stdlib.h>

int len(char *str){
    int len = 0;
    while (str[len] != '\0'){
        len += 1;
    }
    return len;
}

char *double_string(char *str){
    int n = len(str);
    int i;
    char *dbstr;

    dbstr = malloc(n*2);

    for (i = 0; i < n; i++){
        dbstr[i] = str[i];
    }
    for (i = n; i < n*2; i++){
        dbstr[i] = str[i - n];
    }

    return dbstr;
}
int main()
{
    char str[40];
    char *dbstr;

    scanf("%39s", str);

    dbstr = double_string(str);
    printf("Double string: %s\n", dbstr);

    free(double_string(str));

    return 0;
}
