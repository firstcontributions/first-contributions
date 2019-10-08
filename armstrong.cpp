#include<stdio.h>
int main()
{
	int k,a,b,c=0,d,e,f,g,h=0;
	printf("Enter a number:");
	scanf("%d",&a);
	b=a;
	while(b!=0)
	{
		b=b/10;
		c++;
	}
	
	for(d=1;d<=c;d++)
	{
	e=a%10;
	g=e;
		for(f=1;f<c;f++)
		{
			e=g*e;	
		}
	h=h+e;
	a=a/10;
	}

	if(h==k)
	{printf("%d is armstrong number!",h);
	}
	
	else
	{
		printf("%d is not an armstrong number.",h);
	}
}
