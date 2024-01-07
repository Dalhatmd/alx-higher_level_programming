#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted linked list
 *
 * @head: head of the linked list
 * @number: number to be inserted
 *
 * Return: address of new node on success or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
        listint_t *temp = NULL;

	listint_t *new = malloc(sizeof(listint_t));
	if (new == NULL)
		return NULL;
	new->n = number;
	new->next = NULL;
	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return new;
	}
	while (current->next != NULL && number > current->next->n)
	{
		current = current->next;
	}
	temp = current->next;
	current->next = new;
	new->next = temp;
	return new;
}
