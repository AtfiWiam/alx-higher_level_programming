#include<stdio.h>
#include<stdlib.h>
#include <string.h>
#include "lists.h"

/**
 * insert_node - insert node in a linked list
 *
 * @head: pointer to the first node of the linked list
 *
 * @number: integer value of the new node to insert
 *
 * Return: the head of the linked list with the new node inserted
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nh = malloc(sizeof(listint_t));
	listint_t *t = *head;

	if (nh == NULL)
	{
		return (NULL);
	}
	if (t == NULL)
	{
		nh->n = number;
		nh->next = NULL;
		(*head) = nh;
		return (nh);
	}
	if (t->next == NULL || number == 0)
	{
		if (number < t->n)
		{
			nh->n = number;
			nh->next = t;
			(*head) = nh;
			return (nh);
		}
	}
	while (t->next)
	{
		if ((number >= t->n) && (number <= t->next->n))
		{
			nh->n = number;
			nh->next = t->next;
			t->next = nh;
			return (nh);
		}
		t = t->next;
	}
	nh->n = number;
	nh->next = NULL;
	t->next = nh;
	return (nh);
}
