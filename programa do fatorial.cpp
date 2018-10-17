#include <stdio.h>

int main(){
  
     int numero;
  	int i;
  int fatorial;
  
      do {
             printf("Digite um numero inteiro maior ou igual a 0 e eu lhe direi seu fatorial \n");
  		scanf("%d",&numero);
              } while(numero<0);
  int nseipraque = numero; 
          for(i=1;i<nseipraque;i++){
            numero=numero * i; 
                													
          printf("resultado na interaçao %d: %d\n",i,numero);  
            
          }
          
                return 0;
              }
              
