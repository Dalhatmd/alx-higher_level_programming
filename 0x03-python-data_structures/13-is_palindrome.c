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
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *second_half;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	if (fast)
		slow = slow->next;
	second_half = reverse_list(slow);
	while (second_half != NULL)
	{
		if ((*head)->n != second_half->n)
		{
			reverse_list(second_half);
			return (0);
		}
		*head = (*head)->next;
		second_half = second_half->next;
	}
	reverse_list(second_half);
	return (1);
}

/**
 * *reverse_list - Reverses second half of a linked list
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
