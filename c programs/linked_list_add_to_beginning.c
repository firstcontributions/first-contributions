//Take how many elements the user wants to input and then take the elements from the user.Print the Linked List.
#include<stdio.h>
#include<stdlib.h>

    struct node {
        int data;
        struct node *next;
    };


    void addFirst(struct node **head , int val)
    {
        //create a new node .
        struct node *newNode = malloc(sizeof(struct node ));
        newNode->data = val;
        newNode->next = *head;
        *head = newNode;
    }

    void PrintList(struct node *head)
    {
        struct node *temp = head ;
        while(temp!=NULL)
        {
            printf("%d -> ",temp->data);
            temp=temp->next;
        }
        printf("NULL");
    }
  
int main()
{   int val,n,i;

    struct node *head = NULL;
    printf("Enter how many nodes (Enter between 1 and 10 )you want to enter at the beginning : ");
    scanf("%d",&n);
    for(i = 1 ; i<=n ; i++)
    {
        printf("Enter element no : %d ->",i);
        scanf("%d",&val);
        addFirst(&head,val);
    }

    PrintList(head);
    return 0;
}