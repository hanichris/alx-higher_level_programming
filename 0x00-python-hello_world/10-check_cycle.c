#include "lists.h"

/**
 * check_cycle - determines if the linked list has a cycle
 * within it or not.
 * @list: pointer to the head of the linked list.
 * Return: Either 0 or 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr = list;
	listint_t *fast_ptr = list;

	while (fast_ptr && fast_ptr->next)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = (fast_ptr->next)->next;
		if (slow_ptr == fast_ptr)
			return (1);
	}
	return (0);
}
