package com.test.twoDArray;
import java.util.Scanner;
public class TwoDArray {
	public static void main(String[] args) {
int r=4,c=4,i,j,k ;
		int [][] arr  =new int[r][c];
        System.out.println("Enter Elements in Array:");
        Scanner s = new Scanner(System.in);
        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                arr[i][j]=s.nextInt();
            }
        }
	System.out.println("The Given Matrix:");	
for ( i =0 ; i<r ; i ++ ) 
		{
			 for ( j = 0 ; j < c ; j ++ ) 
			 { 
				 System.out.print( arr [ i ] [ j ] + " " )  ; 
				 } 
			 System.out.println( ) ;
			 }
		}
}
