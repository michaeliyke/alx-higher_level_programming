#include "lists.h"

/**
 * print_dlistint - prints all the elements of a dlistint_t list
 * @h: the head pointer
 *
 * Return: number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t n_nodes = 0;
	dlistint_t *tmp;

	if (h == NULL)
		return (n_nodes);
	for (tmp = (dlistint_t *)h; tmp != NULL; tmp = tmp->next, n_nodes++)
		printf("%d\n", tmp->n);
	return (n_nodes);
}
