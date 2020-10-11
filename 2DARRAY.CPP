#include<iostream.h>
#include<conio.h>
#include<string.h>
#include<stdio.h>
int lsearch(int[],int,int);

int main()
{
int ar[50],n,index ,item;

cout<<"enter the size of the string:\n";
cin>>n;
cout<<"enter the string in the array:\n";
for (int i=0; i<n; i++)
{
cin>> ar[i];
}
cout<<"enter the elements to be searched\n";
cin>>item;
index  = lsearch(ar,n,item);
if (index==-1)
{
cout<<"the element not found in the array\n";
}
else
{
cout<<"the elements found at the index of "<<index<<" at postion "<<index+1;
}
return 0;
}

int lsearch(int ar[],int size , int item)
{
for(int i=0; i<size; i++)
{
if  (ar[i]==item)
{
return i;
}
}
return -1;
}

