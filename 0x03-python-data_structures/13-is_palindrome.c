#include "lists.h"

/**
 * is_palindrome -  checks if a singly linked list is a palindrome
 * @h: the head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 * NOTE:
 * 1. use fast-slow steps to get the middle and the end.
 * 2. reverse the 2nd half of the list in place,
 * this splits the list in two halfs with the 2nd half reversed
 * 3. check if the elements of both match
 *
 * REVERSE THE SECOND HALF
 * STEPS:
 * 1. save the next spot in a variable
 * 2. put both slow and temp on the next of that variable
 * LOOP:
 * Advance slow to the next of slow and assign the next of temp to that vriable
 * assign that variable to temp, assign temp to slow
 */
int is_palindrome(listint_t **h)
{
	listint_t *fast, *slow, *hh, *old;

	if (h == NULL || *h == NULL) /* If no elemnts */
		return (1);

	if (!((*h)->next)) /* if only one element */
		return (1);
	if (!((*h)->next->next)) /* if only two elements */
		return ((*h)->next->n == (*h)->n);

	slow = *h;
	fast = (*h)->next->next;
	/* At least 3 elems, drive fast to the end and slow to the middle */
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next;
		if (fast->next)
			fast = fast->next;
	}

	old = slow; /* end of first half */
	hh = fast->next == NULL ? slow : slow->next;
	slow = fast = slow->next;

	old->next = NULL;
	hh->next = NULL;
	while (fast)
	{
		slow = slow->next;
		fast->next = hh;
		hh = fast;
		fast = slow;
	}
	for (old = *h; old && hh; old = old->next, hh = hh->next)
		if (old->n != hh->n)
			return (0);
	return (1);
}
