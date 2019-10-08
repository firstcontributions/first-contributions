#include <stdio.h>
int main()
{
	int a=0,b=1,i=0,j,n,f;
	printf("Enter a number:");
	scanf("%d",&n);
	while(i!=n)
	{
		printf(" %d ",a);
		f=a+b;
		a=b;
		b=f;
		i++;                                                                                                      
		
	}
return 0;
}
