#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - determines whether a linked list is a palindrome or not.
 * @head: address of the pointer to the head of the linked list.
 * Return: Either 0 or 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast_ptr = *head;
	listint_t *slow_ptr = *head;
	listint_t *pre_slow_ptr = *head;
	listint_t *mid_node = NULL;
	int res = 1;

	if (*head && (*head)->next)
	{
		while (fast_ptr && fast_ptr->next)
		{
			fast_ptr = (fast_ptr->next)->next;
			pre_slow_ptr = slow_ptr;
			slow_ptr = slow_ptr->next;
		}
		if (fast_ptr)
		{
			mid_node = slow_ptr;
			slow_ptr = slow_ptr->next;
		}
		pre_slow_ptr->next = NULL;
		reverse(&slow_ptr);
		res = compare(*head, slow_ptr);
		reverse(&slow_ptr);
		if (mid_node)
		{
			pre_slow_ptr->next = mid_node;
			mid_node->next = slow_ptr;
		}
		else
			pre_slow_ptr->next = slow_ptr;
	}
	return (res);
}

/**
 * reverse - reverses a linked list.
 * @head: address of the pointer to the head of the linked list.
 */
void reverse(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *nxt = NULL;

	while (*head)
	{
		nxt = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = nxt;
	}
	*head = prev;
}

/**
 * compare - compares two linked lists of equal length to determine
 * if they are the same.
 * @head1: pointer to the head of the first linked list.
 * @head2: pointer to the head of the second linked list.
 * Return: Either 0 or 1.
 */
int compare(listint_t *head1, listint_t *head2)
{
	listint_t *first_half = head1;
	listint_t *second_half = head2;

	while (first_half && second_half)
	{
		if (first_half->n != second_half->n)
			return (0);
		first_half = first_half->next;
		second_half = second_half->next;
	}
	return (1);
}
