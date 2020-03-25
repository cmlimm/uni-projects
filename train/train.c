#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_IMMORTALS 10

typedef struct carriage {
	char *number;
    int n_immortals;
    char *immortals[MAX_IMMORTALS];
    char *isPotionHere;
	struct carriage * next;
} carriage;

void display(carriage *start){
	carriage *i = start;
    int k;
	for ( ; i != NULL; i=i->next){ /* i=(*i).next */
        printf("Number of carriage: %s\n", i->number);
		printf("Number of immortals: %d\nImmortals: ", i->n_immortals);
        for (k = 0; k < i->n_immortals; k++){
            if (k != i->n_immortals - 1)
                printf("%s, ", i->immortals[k]);
            else
                printf("%s\n", i->immortals[k]);
        }
        printf("Is Potion of Immortality in this carriage? ");
        printf("%s\n", i->isPotionHere);
	}
}

carriage *add_carriage(){
	carriage *new = malloc(sizeof(carriage));
    int i, n;
    char name[30];
    char new_number[30];
    char flag[4];

    printf("Enter number of carriage: ");
    scanf("%29s", new_number);
    new->number = new_number;

    printf("Enter number of immortal: ");
    scanf("%d", &n);
    new->n_immortals = n;

    if (n != 0){
        printf("Enter names of immortals: ");
        for (i = 0; i < new->n_immortals; i++){
            scanf("%29s", name);
            new->immortals[i] = malloc(strlen(name) + 1);
            strcpy(new->immortals[i], name);
        }
    }
    printf("Is Potion of Immortality in this carriage? ");
    scanf("%3s", flag);
    new->isPotionHere = flag;

    new->next = NULL;

	return new;
}

void release(carriage *start){

	carriage *i = start;
	carriage *next = NULL;
    int k;

	for ( ; i != NULL ; i = next){
		next = i->next;
        for (k = 0; k < i->n_immortals; k++){
            free(i->immortals[k]);
        }
		free(i);
	}
}

int main(){
	carriage *start = NULL;

	start = add_carriage();

	display(start);
	release(start);

return 0;

}
