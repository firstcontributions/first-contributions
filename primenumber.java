package com.journaldev.javaprograms;

import java.util.Scanner;

public class CheckPrimeNumber {

	public static void main(String[] args) {

		Scanner s = new Scanner(System.in);
		System.out.print("Enter number to check for prime:");
		int n = s.nextInt();
		s.close();
		checkPrime(n);
	}

	private static void checkPrime(int n) {
		if (n == 0 || n == 1) {
			System.out.println(n + " is not a prime number");
			return;
		}
		if (n == 2) {
			System.out.println(n + " is a prime number");
		}
		for (int i = 2; i <= n / 2; i++) {
			if (n % i == 0) {
				System.out.println(n + " is not a prime number");
				return;
			}
		}
		System.out.println(n + " is a prime number");
	}

}
