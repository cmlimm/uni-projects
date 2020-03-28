#include <stdio.h>

int len(char *str){
    int len = 0;
    while (str[len] != '\0'){
        len += 1;
    }
    return len;
}

int str_to_int(char *str){
    int n = len(str);
    int i;
    int number = 0;
    int factor = 1;

    for (i = n - 1; i >= 0; i--){
        if (str[i] == '1'){
            number += 1*factor;
            factor *= 10;
        }
        if (str[i] == '2'){
            number += 2*factor;
            factor *= 10;
        }
        if (str[i] == '3'){
            number += 3*factor;
            factor *= 10;
        }
        if (str[i] == '4'){
            number += 4*factor;
            factor *= 10;
        }
        if (str[i] == '5'){
            number += 5*factor;
            factor *= 10;
        }
        if (str[i] == '6'){
            number += 6*factor;
            factor *= 10;
        }
        if (str[i] == '7'){
            number += 7*factor;
            factor *= 10;
        }
        if (str[i] == '8'){
            number += 8*factor;
            factor *= 10;
        }
        if (str[i] == '9'){
            number += 9*factor;
            factor *= 10;
        }
        if (str[i] == '0')
            factor *= 10;
    }

    return number;
}
