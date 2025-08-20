//create a calculatir

import java.util.Scanner;

public class Calc {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter first number:");
        double num1 = scanner.nextDouble();
        System.out.println("Enter second number:");
        double num2 = scanner.nextDouble();
        System.out.println("Choose an operation: +, -, *, /");
        char operation = scanner.next().charAt(0);
        double result;
        switch (operation) {
            case '+':
                result = num1 + num2;
                break;
            case '-':
                result = num1 - num2;
                break;
            case '*':
                result = num1 * num2;
                break;
            case '/':
                if (num2 != 0) {
                    result = num1 / num2;
                } else {
                    System.out.println("Error: Division by zero is not allowed.");
                    return;
                }
            default:
                System.out.println("Error: Invalid operation.");
                return;
        }
        System.out.println("Result: " + result);
        scanner.close();
    }
}
