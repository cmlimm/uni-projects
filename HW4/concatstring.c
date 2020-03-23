#include <stdio.h>
#include <stdlib.h>

int len(char *str){
    int len = 0;
    while (str[len] != '\0'){
        len += 1;
    }
    return len;
}

char *concat_string(char *str1, char *str2){
    int n1 = len(str1);
    int n2 = len(str2);
    int i;
    char *concat = malloc(n1 + n2);

    for (i = 0; i < n1; i++){
        concat[i] = str1[i];
    }
    for (i = 0; i < n2; i++){
        concat[n1 + i] = str2[i];
    }

    return concat;
}
int main()
{
    char str1[40];
    char str2[40];
    char *concat;

    scanf("%39s", str1);
    scanf("%39s", str2);

    concat = concat_string(str1, str2);

    printf("Concatenated strings: %s\n", concat);

    free(concat);

    return 0;
}
