#include<stdio.h>
#include<stdlib.h>
struct node * f=NULL;
struct node * r=NULL;
struct node {
    int size;
    struct node *link;
    int data;
};
void linkedtraversal(struct node * ptr)
{
    while(ptr!=NULL)
    {
        printf("elements in the linked list is%d\n",ptr->data);
        ptr=ptr->link;
    }
}
int isFull()
{
    struct node * n=(struct node *)malloc(sizeof(struct node));
    if(n==NULL)
    {
        return 1;
    }
    else
    {
        return 0;
    }
    
    
}
int isEmpty(struct node * f)
{
    if(f==NULL)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
void equene(int val)
{
    struct node * n=(struct node *)malloc(sizeof(struct node));
    if(n==NULL)
    {
        printf("quene is FULl");
    }
    
    else
    {
        
        n->data=val;
        n->link=NULL;
        if(f==NULL)
        {
            f=r=n;
        }
        else
        {
            r->link=n;
            r=n;
        }
    }
}
int dequene()
{
    int a=-1;
    struct node * ptr=f;
    if(isEmpty(f))
    {
        printf("quene underflow\n");
    }
    else
    {
        f=f->link;
        a=ptr->data;
        free(ptr);
    }
    return a;
}


int main()
{
    linkedtraversal(f);
    equene(45);
    equene(70);
    equene(80);
    
    linkedtraversal(f);
    printf("dequqeing elements %d\n",dequene());
    printf("dequqeing elements %d\n",dequene());
    
    return 0;
}
