package Options;

import java.text.DecimalFormat;
import java.util.Scanner;

//Here the user will input all the details
public class Inputs {
	public static Scanner sc = new Scanner(System.in);
	
	//User chooses what they want to do
	public static int Selection() {
		
		int Choice;
		
		System.out.println();
		System.out.println("Which of the following are you interested in finding?: ");
		System.out.println("(1) Potential profit for a given trade: ");
		System.out.println("(2) Potential profit for a covered call/put: ");
		System.out.println("(0) Exit");
		
		Choice = sc.nextInt();
		
		if(Choice < 0 || Choice > 2) {
			System.out.println("INVALID");
			Selection();
		}
		return Choice;
	}
	
	public static void InputValues() {
		
		//Scanning the main values
		System.out.println("Enter the asking Price: ");
		Formulae.Ask = sc.nextDouble();
		System.out.println("Enter the Delta: ");
		Formulae.Delta = sc.nextDouble();
		System.out.println("Enter the number of contracts bought: ");
		Formulae.Contracts = sc.nextInt();
	}
}
