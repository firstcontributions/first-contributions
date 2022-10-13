// C program to check if the linked list is circular
#include <stdio.h>
#include <stdlib.h>

struct Node {
	int data;
	struct Node* next;
};

int isCircular(struct Node* head)
{
	// If linked list is empty it is circular
	if (head == NULL)
		return 1;
	struct Node* ptr;
	ptr = head->next;
	// Traversing linked list till last node
	while (ptr != NULL && ptr != head)
		ptr = ptr->next;
	// Condition for circular linked list
	return (ptr == head);
}
// Function to create new Node
struct Node* newnode(int data)
{
	struct Node* temp;
	temp = (struct Node*)malloc(sizeof(struct Node));
	temp->data = data;
	temp->next = NULL;
	return temp;
}

// Driver's code
int main()
{
	// code
	// Starting with empty list
	struct Node* head = newnode(1);
	head->next = newnode(2);
	head->next->next = newnode(3);
	head->next->next->next = newnode(4);

	// Checking for circular list
	if (isCircular(head))
		printf("Yes\n");
	else
		printf("No\n");

	// If not circular making it circular
	head->next->next->next->next = head;
	if (isCircular(head))
		printf("Yes\n");
	else
		printf("No\n");
	return 0;
}
