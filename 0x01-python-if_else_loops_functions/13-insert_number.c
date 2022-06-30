#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert a node into a sorted linked list.
 * @head: pointer to the pointer to the head of the linked list.
 * @number: number to be inserted into the linked list.
 * Return: address of the inserted node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = NULL;
	listint_t *curr = *head;

	temp = malloc(sizeof(listint_t));
	if (!temp)
		return (NULL);

	temp->n = number;
	temp->next = NULL;

	if (!*head)
	{
		*head = temp;
		return (temp);
	}
	if (temp->n < curr->n)
	{
		temp->next = *head;
		*head = temp;
		return (temp);
	}

	while (curr->next)
	{
		if ((curr->n <= temp->n) &&
		    (temp->n <= curr->next->n))
		{
			temp->next = curr->next;
			curr->next = temp;
			return (temp);
		}
		curr = curr->next;
	}
	curr->next = temp;
	return (temp);
}
