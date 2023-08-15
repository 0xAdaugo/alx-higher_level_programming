#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>


/**
 * struct listint_s - Represents a node in a singly linked list.
 * @n:Integer value stored in the node.
 * @next: Pointer to the next node on the  list.
 *
 * Description: This structure defines a node for a dingly linked lists
 * used in the project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

#endif /* LISTS_H */
