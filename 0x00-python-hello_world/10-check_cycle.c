#include "lists.h"
/**
 * check_cycle - checks if a linked list contains a cycle
 *
 * @list: list to be checked
 *
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *var;
	listint_t *check;

	var = list;
	check = list;
	while (var != NULL)
	{
		var = var->next;
		if (var == check)
		{
			return (1);
		}
	}
	return (0);
}
