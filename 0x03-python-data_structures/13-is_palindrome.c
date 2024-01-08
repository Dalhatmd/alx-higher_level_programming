#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 * is_palindrome - checks if a linked list is a palindrome
 *
 * @head: head of the linked list
 *
 * Return: 0 if it is not a palindrome and 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *reverse = NULL;
	listint_t **list = NULL;
	int i = 0;
	int j, k;

	while (current != NULL)
	{
		current = current->next;
		i++;
	}
	list = malloc(i * sizeof(listint_t *));
	if (list == NULL)
		return 0;
	current = *head;
	for (j = 0; j < i; j++)
	{
		list[j] = current;
		current = current->next;
	}
	reverse = reverse_list(*head);
	for (k = 0; k < i; k++)
	{
		if (reverse->n != list[k]->n)
		{
			free(list);
			return 0;
		}
		reverse = reverse->next;
	}
	free(list);
	return 1;
}

/**
 * *reverse_list - Reverses a linked list
 *
 * @head: head of the list
 *
 * Return: returns the new head of the list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}
