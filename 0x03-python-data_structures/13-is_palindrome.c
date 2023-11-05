#include "lists.h"

/**
 * is_palindrome -  checks if a singly linked list is a palindrome
 * @h: the head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 * @NOTE:
 * 1. use fast-slow steps get the middle and the end.
 * 2. reverse the 2nd half of the list in place,
 * this splits the list in two halfs with the 2nd half reversed
 * 3. check if the elements of both match
 */
int is_palindrome(listint_t **h)
{
	listint_t *fast, *slow, *nh;

	if (h == NULL || *h == NULL)
		return (1);
	fast = *h;
	slow = *h;
	if (!(fast = fast->next)) /* if only one element */
		return (1);
	if (!(fast = fast->next)) /* if there are only two elements */
		return (fast->n == slow->n);

	/**
	 * there's at least three elements
	 * drive fast to the end and slow to almost the middle
	 */
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next;
		if (fast->next)
			fast = fast->next;
	}

	/* Reverse the second half */
	nh = new_listint();

	while (slow)
	{
	}
}

/**
 * new_listint - make a new listint linked list
 *
 * Return: pointer to a new listint linked list
 */
listint_t *new_listint(void)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
}
