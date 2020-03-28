#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_passengers 10

/*
 * Struct: carriage
 * name: string, name of the carriage
 * n_passengers: integer number of passengers in the carriage
 * passengers: string array, names of passengers
 * isTreasureHere: string, inforamation whether treasure
 *                 in this carriage or not, "Yes" or "No"
 * prev: link to the previous element of the doubly linked list
 * next: link to the next element of the doubly linked list
 */
typedef struct carriage {
    char *name;
    int n_passengers;
    char *passengers[MAX_passengers];
    char *isTreasureHere;
    struct carriage * prev;
	struct carriage * next;
} carriage;

/*
 * Function: display
 * -----------------
 * displays contents of doubly linked list of carriage elements
 *
 * start: firslt element of linked list
 *
 * returns: nothing
 */
void display(carriage *start){
	carriage *i = start;
    int k;

	for ( ; i != NULL; i=i->next){

        printf("Number of carriage: ");
        printf("%s\n", i->name);

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

/*
 * Function: add_carriage
 * -----------------
 * adds new element to doubly linked list of carriage elements
 *
 * last: last element of the linked list
 *
 * returns: link to newly created carriage
 */
carriage *add_carriage(carriage *last){
	carriage *new = malloc(sizeof(carriage));
    int i, n;
    char passenger_name[30];
    char isTreasureHere[4];
    char carriage_name[30];

    printf("Enter number of carriage: ");
    scanf("%29s", carriage_name);
    /* allocate memory for string */
    new->name = malloc(strlen(carriage_name) + 1);
    strcpy(new->name, carriage_name);

    while (1){
        printf("Enter number of passengers: ");
        scanf("%d", &n);
        if (n <= MAX_passengers){
            new->n_passengers = n;
            break;
        }
        printf("Too many passengers.\n");
    }

    if (n != 0){
        printf("Enter names of passengers: ");
        for (i = 0; i < new->n_passengers; i++){
            scanf("%29s", passenger_name);
            /* allocate memory for string */
            new->passengers[i] = malloc(strlen(passenger_name) + 1);
            strcpy(new->passengers[i], passenger_name);
        }
    }

    printf("Is Treasure in this carriage? ");
    scanf("%3s", isTreasureHere);
    /* allocate memory for string */
    new->isTreasureHere = malloc(strlen(isTreasureHere) + 1);
    strcpy(new->isTreasureHere, isTreasureHere);

    /* as it is the last element of the linked list, there is no next element */
    new->next = NULL;

    /*
        if it wasn't the first element of the list, then it is possible
        to specify previous element and change previous element's link to
        the next element to this element

        else set link to previous element to NULL
    */
    if (last != NULL){
        last->next = new;
        new->prev = last;
    }
    else new->prev = NULL;

	return new;
}

/*
 * Function: destroy
 * -----------------
 * removes elements starting from start
 *
 * start: first element to remove
 *
 * returns: new last element of the list, if there is none, returns NULL
 */
carriage *destroy(carriage *start){
	carriage *i = start;
	carriage *next = NULL;
    carriage *prev = NULL;
    int k;

	for ( ; i != NULL ; i = next){
		next = i->next;
        for (k = 0; k < i->n_passengers; k++){
            free(i->passengers[k]);
        }
        free(i->name);
        free(i->isTreasureHere);
        /*
            if there is previous element then we are not removing an entire list,
            so we need to change link of the previous element to the next
            element to NULL, as there is no next element anymore
        */
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
        printf("\n");

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
            last = destroy(last);
            if (last != NULL){
                if (last->prev == NULL)
                    start = NULL;
            }
        }

        //destroy train
        if (command == '4'){
            last = destroy(start);
            start = NULL;
        }

        //exit
        if (command == '5'){
            destroy(start);
            break;
        }
        printf("\n");
    }

    printf("Train destroyed\n");

return 0;

}
