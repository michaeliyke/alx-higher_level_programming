#include "lists.h"

/**
 * dlistint_len - returns the number of elements in a linked dlistint_t list
 * @h: pointer to the head
 *
 * Return: size/length of the list
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t size;
	dlistint_t *tmp;

	for (size = 0, tmp = (dlistint_t *)h; tmp != NULL; tmp = tmp->next, size++)
		;
	return (size);
}
