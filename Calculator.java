package first_contributions;

public class Calculator {

   // Original add method
public double add(double a, double b) {
    return a + b; // intentionally modified to cause conflict
}


    // Subtract method
    public double subtract(double a, double b) {
        return a - b;
    }

    // Multiply method
    public double multiply(double a, double b) {
        return a * b;
    }

    // Divide method
    public double divide(double a, double b) {
        if (b == 0) {
            throw new IllegalArgumentException("Division by zero is not allowed.");
        }
        return a / b;
    }
}
