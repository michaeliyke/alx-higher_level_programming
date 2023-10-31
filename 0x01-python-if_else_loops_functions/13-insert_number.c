#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node -  inserts a number into a sorted singly linked list
 * @head: pointer to the head of the list
 * @number: the number to insert
 *
 * Return: pointer to the newly inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new, *prev;

	new = malloc(sizeof(listint_t));

	if (head == NULL || new == NULL)
		return (0);

	new->n = number;
	new->next = NULL;
	current = *head;
	prev = NULL;

	for (; current; prev = current, current = current->next)
	{
		if (current->n > number)
		{
			if (prev)
				prev->next = new;
			else
				*head = new;
			new->next = current;
			return (new);
		}
		if (current->next == NULL)
		{
			current->next = new;
			return (new);
		}
	}
	/* Here, current is NULL */
	*head = new;
	return (new);
}
