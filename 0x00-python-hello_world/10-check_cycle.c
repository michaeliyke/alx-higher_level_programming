#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: a singly linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 * s moves slowly taking single step each time f moves double steps once
 * If they both ever meet, there is a cycle and it's junction can be found
 * by placing either variable at the head with other still at their last spot.
 * Then both should be advanced forward a step at a time.
 * With this, when the variables meet again, it is at the very junction
 * of the loop.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!(list && list->next && list->next->next))
		return (0);

	slow = list->next, fast = list->next->next;
	for (; fast && fast->next; slow = slow->next, fast = fast->next->next)
		if (slow->n == fast->n)
			return (1);
	return (0);
}
