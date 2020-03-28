#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "str_to_int.h"
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
    struct carriage * prev;
	struct carriage * next;
} carriage;

/*
 * Function: print
 * -----------------
 * prints contents of one carriage
 *
 * crrg: carriage to print
 *
 * returns: nothing
 */
void print(carriage *crrg){
    printf("Number of carriage: ");
    printf("%s\n", crrg->name);

    printf("Number of passengers: %d\nPassengers: ", crrg->n_passengers);
    for (k = 0; k < crrg->n_passengers; k++){
        if (k != crrg->n_passengers - 1)
            printf("%s, ", crrg->passengers[k]);
        else
            printf("%s\n", crrg->passengers[k]);
    }
}

/*
 * Function: display
 * -----------------
 * prints contents of doubly linked list of carriage elements
 *
 * start: firslt element of linked list
 *
 * returns: nothing
 */
void display(carriage *start){
	carriage *i = start;
    int k;

	for ( ; i != NULL; i=i->next){
        print(i);
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
    char carriage_name[30];
    char passenger_name[30];

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

/*
 * Function: find_name
 * -----------------
 * finds carriage with specified name
 *
 * start: first element of the list
 * name: name to find
 *
 * returns: first carriage with specidied name
 */
carriage *find_name(carriage *start, char *name){
    carriage *target = NULL;

    for ( ; i != NULL ; i=i->next){
        if (i->name == name){
            target = i;
            break;
        }
    }

    return target;
}

/*
 * Function: find_number
 * -----------------
 * finds carriage with specified number of passengers
 *
 * start: first element of the list
 * number: number of passengers to find
 *
 * returns: first carriage with specidied number of passengers
 */
carriage *find_number(carriage *start, int number){
    carriage *target = NULL;

    for ( ; i != NULL ; i=i->next){
        if (i->n_passengers == name){
            target = i;
            break;
        }
    }

    return target;
}

/*
 * Function: find_min
 * -----------------
 * finds carriage with minimum number of passengers
 *
 * start: first element of the list
 *
 * returns: first carriage with minimum number of passengers
 */
carriage *find_min(carriage *start){
    carriage *target = NULL;
    int min = MAX_passengers + 1;

    for ( ; i != NULL ; i=i->next){
        if (i->n_passengers < min){
            target_min = i;
            min = i->n_passengers;
        }
    }

    return target;
}

/*
 * Function: find_min
 * -----------------
 * finds carriage with maximum number of passengers
 *
 * start: first element of the list
 *
 * returns: first carriage with maximum number of passengers
 */
carriage *find_max(carriage *start){
    carriage *target = NULL;
    int max = -1;

    for ( ; i != NULL ; i=i->next){
        if (i->n_passengers > max){
            target_max = i;
            max = i->n_passengers;
        }
    }

    return target
}

int main(){
	carriage *start = NULL;
    carriage *last = NULL;
    carriage *new = NULL;
    carriage *target = NULL;
    char command;
    char sub_command;
    char name[30];
    char *help;
    int number;

    help = "Add carriage to the train (1)\n"
           "Show every carriage info (2)\n"
           "Destroy last carriage (3)\n"
           "Destroy train (4)\n"
           "Find carriage by name (5)\n"
           "Find carriage by number of passengers (6)\n"
           "Exit (7)\n";

    while (1){
        printf("%s", help);
        printf("Enter command number: ");
        scanf(" %c", &command);
        printf("\n");

        /* add carriage */
        if (command == '1'){
            printf("Add carriage to the end of the train (1)\n"
                   "Add carriage after carriage with specified name (2)\n")
            new = add_carriage(last);
            if (start == NULL)
                start = new;
            last = new;
        }

        /* show every carriage info */
        if (command == '2')
            display(start);

        /* destroy last carriage */
        if (command == '3'){
            last = destroy(last);
            if (last != NULL){
                if (last->prev == NULL)
                    start = NULL;
            }
        }

        /* destroy train */
        if (command == '4'){
            last = destroy(start);
            start = NULL;
        }

        /* find carriage by name */
        if (command == '5'){
            printf("Enter name: ");
            scanf("%29s", name);
            target = find_name(start, name);
            print(target);
        }

        /* find carriage by number of passengers */
        if (command == '6'){
            printf("Find carriage with:\n"
                   "\tmaximum number of passengers (1)\n"
                   "\tminimum number of passengers (2)\n"
                   "\tspecific number of passengers (3)\n")
            scanf(" %c", sub_command);

            if (sub_command == '1')
                target = find_max(start);
            if (sub_command == '2')
                target = find_min(start);
            if (sub_comman == '3'){
                printf("Enter number of passengers: ");
                scanf("%d", &number);
                target = find_number(start, number);
            }

            if (target != NULL)
                print(target);
            else
                printf("No carriage with specified parameters.\n")
        }

        /* exit */
        if (command == '7'){
            destroy(start);
            break;
        }
        printf("\n");
    }

    printf("Train destroyed\n");

return 0;

}
