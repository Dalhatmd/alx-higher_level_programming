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
	listint_t *slow;
	listint_t *fast;

	if (list == NULL)
	{
		return (0);
	}
	slow = list;
	fast = list;
	while (fast != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
