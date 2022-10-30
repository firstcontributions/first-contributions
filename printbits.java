// Java application to print Binary represntation of the given input [ Any input ] 


import java.lang.System;
import java.util.Scanner;
import java.lang.Integer;
import java.lang.Double;

public class printbits
{
	public static void main(String[] args) 
	{
		

	    Scanner pb = new Scanner(System.in);
		String decimal = pb.next();
	try
	{
		if(decimal.contains("."))
		{   
            System.out.println("ERROR");
			System.exit(0);
		}
		else if(!(decimal.contains(".")))
		{
				int b = Integer.parseInt(decimal);
				System.out.println(Integer.toBinaryString(b));
				System.exit(0);
		}
	}
	catch(NumberFormatException e)
	{
        System.out.println("ERROR");
	}
            
	}
	
}
