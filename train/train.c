#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_passengers 10

typedef struct carriage {
    char *number;
    int n_passengers;
    char *passengers[MAX_passengers];
    char *isTreasureHere;
    struct carriage * prev;
	struct carriage * next;
} carriage;

void display(carriage *start){
	carriage *i = start;
    int k;

	for ( ; i != NULL; i=i->next){ /* i=(*i).next */

        printf("Number of carriage: ");
        printf("%s\n", i->number);

		printf("Number of passengers: %d\nPassengers: ", i->n_passengers);
        for (k = 0; k < i->n_passengers; k++){
            if (k != i->n_passengers - 1)
                printf("%s, ", i->passengers[k]);
            else
                printf("%s\n", i->passengers[k]);
        }
        printf("Is Treasure in this carriage? ");
        printf("%s\n\n", i->isTreasureHere);
	}
}

carriage *add_carriage(carriage *last){
	carriage *new = malloc(sizeof(carriage));
    int i, n;
    char name[30];
    char isTreasureHere[4];
    char number[30];

    printf("Enter number of carriage: ");
    scanf("%29s", number);
    new->number = malloc(strlen(number) + 1);
    strcpy(new->number, number);

    printf("Enter number of passengers: ");
    scanf("%d", &n);
    new->n_passengers = n;

    if (n != 0){
        printf("Enter names of passengers: ");
        for (i = 0; i < new->n_passengers; i++){
            scanf("%29s", name);
            new->passengers[i] = malloc(strlen(name) + 1);
            strcpy(new->passengers[i], name);
        }
    }

    printf("Is Treasure in this carriage? ");
    scanf("%3s", isTreasureHere);
    new->isTreasureHere = malloc(strlen(isTreasureHere) + 1);
    strcpy(new->isTreasureHere, isTreasureHere);

    new->next = NULL;

    if (last != NULL){
        last->next = new;
        new->prev = last;
    }
    else new->prev = NULL;

	return new;
}

carriage *release(carriage *start){
	carriage *i = start;
	carriage *next = NULL;
    carriage *prev = NULL;
    int k;

	for ( ; i != NULL ; i = next){
		next = i->next;
        for (k = 0; k < i->n_passengers; k++){
            free(i->passengers[k]);
        }
        free(i->number);
        free(i->isTreasureHere);
        if (i->prev != NULL){
            i->prev->next = NULL;
            prev = i->prev;
        }
		free(i);
	}

    return prev;
}

int main(){
	carriage *start = NULL;
    carriage *last = NULL;
    carriage *new = NULL;
    char command;
    char *help;

    help = "Add carriage to the train (1)\n"
           "Show every carriage info (2)\n"
           "Destroy last carriage (3)\n"
           "Destroy train (4)\n"
           "Exit (5)\n";

    while (1){
        printf("%s", help);
        printf("Enter command number: ");
        scanf(" %c", &command);

        //add carriage
        if (command == '1'){
            new = add_carriage(last);
            if (start == NULL)
                start = new;
            last = new;
        }

        //show every carriage info
        if (command == '2')
            display(start);

        //destroy last carriage
        if (command == '3'){
            last = release(last);
            if (last != NULL){
                if (last->prev == NULL)
                    start = NULL;
            }
        }

        //destroy train
        if (command == '4'){
            last = release(start);
            start = NULL;
        }

        //exit
        if (command == '5'){
            release(start);
            break;
        }
        printf("\n");
    }

    printf("Train destroyed\n");

return 0;

}
