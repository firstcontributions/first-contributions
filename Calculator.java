package first_contributions;

public class Calculator {

    // Add method
    public double add(double a, double b) {
        return a + b;
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
