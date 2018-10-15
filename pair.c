#include<stdio.h>
int main()
{
    int a[100],n,k,i,j,l=0;
    scanf("%d %d",&n,&k);
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
   for(i=0;i<n;i++)
   {
    for(j=i+1;j<n;j++)
    {
        if((a[i]+a[j])%k==0)
            l++; 
    }
   }
    printf("%d",l);
    
}
