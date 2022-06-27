#include "lists.h"

/**
 * _check_cycle - iterator
 * *list: listint_t *
 * *head: listint_t *(the address of the first listint_t in the cycle)
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int _check_cycle(listint_t *list, listint_t *head)
{
	if (*list->next == NULL)
		return (0);
	else if (*list->next == &head)
		return (1);

	return _check_cycle(list->next, &head);
}

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: listint_t *
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	if (list == NULL)
		return (0);

	return (_check_cycle(&list, &list));
}
