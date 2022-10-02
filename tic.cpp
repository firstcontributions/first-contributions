/*# Tic-Tac-Toa-Game A Simple game using C language as a weapon........*/ #include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<stdio.h>
using namespace std;
char a[3][3];
 void display() 
 { cout<<"\n------------------\n";
   cout<<"\n "<<a[0][0]<<" | "<<a[0][1]<< " | "<<a[0][2];
   cout<<"\n------------------\n"; 
   cout<<"\n "<<a[1][0]<<" | "<<a[1][1]<< " | "<<a[1][2]; 
   cout<<"\n------------------\n";
   cout<<"\n "<<a[2][0]<<" | "<<a[2][1]<< " | "<<a[2][2];
   cout<<"\n------------------\n"; }
  int win() 
  { 
    if((a[0][0]==a[0][1]&&a[0][1]==a[0][2])||(a[0][0]==a[1][0]&&a[1][0]==a[2][0])||(a[0][1]==a[1][1]&&a[1][1]==a[2][1])||(a[0][2]==a[1][2]&&a[1][2]==a[2][2])||(a[2][0]==a[2][1]&&a[2][1]==a[2][2])||(a[1][0]==a[1][1]&&a[1][1]==a[1][2])||(a[0][0]==a[1][1]&&a[1][1]==a[2][2])||(a[0][2]==a[1][1]&&a[1][1]==a[2][0])) return 1;
   else return 0; 
   }
    int main() { 
       a[0][0]='1';
       a[0][1]='2'; 
       a[0][2]='3';
       a[1][0]='4';
       a[1][1]='5'; 
       a[1][2]='6'; 
       a[2][0]='7';
       a[2][1]='8'; 
       a[2][2]='9'; 
      printf("\033c"); 
      display(); 
     int count=0,n,x; 
     char val;
    
    while(count!=9)
     { 
        if(count%2==0) val='x'; else val='0'; 
        cin>>n;
         printf("\033c"); 
         switch(n) { 
          case 1: 
               count++;
               a[0][0]=val;
               display();
               x=win();
             if(x==1) 
             { 
                if(count%2==1) 
                   printf("player 1 win");
                else printf("player 2 win");
                   exit(0); 
              } 
                      break;
          case 2: 
                    count++;
                    a[0][1]=val; display();
                    x=win();
                    if(x==1) { 
                      if(count%2==1) 
                       printf("player 1 win");
                       else 
                      printf("player 2 win");
                      exit(0); 
                      } 
                      break; 
          case 3: 
              count++;
              a[0][2]=val;
              display();
              x=win(); 
              if(x==1) 
              {
                if(count%2==1) 
                  printf("player 1 win"); 
                else 
                  printf("player 2 win");
                  exit(0);
                      } 
                break; 
            case 4: 
              count++;
             a[1][0]=val;
             display();
             x=win(); 
             if(x==1) 
             {
                 if(count%2==1) 
                 printf("player 1 win");
                 else 
                 printf("player 2 win");
                 exit(0); 
                 }
                 break; 
             case 5:
                  count++;
                   a[1][1]=val; 
                   display();
                   x=win();
                   if(x==1) {
                      if(count%2==1) 
                         printf("player 1 win");
                      else 
                         printf("player 2 win");
                         exit(0);
                        } 
                       break;
              case 6: 
                         count++;
                         a[1][2]=val;
                          display();
                          x=win();
                          if(x==1) 
                            { 
                            if(count%2==1) 
                              printf("player 1 win");
                            else 
                              printf("player 2 win"); 
                             exit(0);
                              }
                              break;
                case 7: 
                        count++;
                        a[2][0]=val; 
                        display();
                        x=win();
                        if(x==1) 
                        { 
                        if(count%2==1) 
                            printf("player 1 win");
                        else 
                            printf("player 2 win"); 
                            exit(0);
                        } 
                        break;
                case 8: 
                        count++;
                        a[2][1]=val; 
                        display();
                        x=win();
                        if(x==1) { 
                        if(count%2==1) 
                          printf("player 1 win");
                        else
                          printf("player 2 win");
                        exit(0);
                        } 
                        break;
                case 9:
                        count++;
                        a[2][2]=val;
                        display();
                        x=win();
                        if(x==1) { 
                            if(count%2==1) 
                                printf("player 1 win");
                            else 
                                printf("player 2 win");
                                exit(0);
                                } 
                                break;
                            }
                            } 
    printf("draw");
    return 0;
    }