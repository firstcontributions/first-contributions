
public class BridgePatternExample {

    interface Color {

        String applyColor();
    }

    static class RedColor implements Color {

        @Override
        public String applyColor() {
            return "Red";
        }
    }

    static class BlueColor implements Color {

        @Override
        public String applyColor() {
            return "Blue";
        }
    }

    abstract static class Shape {

        protected Color color;

        public Shape(Color color) {
            this.color = color;
        }

        abstract String draw();
    }

    static class Circle extends Shape {

        public Circle(Color color) {
            super(color);
        }

        @Override
        String draw() {
            return "Drawing a Circle with color " + color.applyColor();
        }
    }

    static class Square extends Shape {

        public Square(Color color) {
            super(color);
        }

        @Override
        String draw() {
            return "Drawing a Square with color " + color.applyColor();
        }
    }

    public static void main(String[] args) {
        Color redColor = new RedColor();
        Color blueColor = new BlueColor();
        Circle circle = new Circle(redColor);
        Square square = new Square(blueColor);
        System.out.println(circle.draw()); // Output: Drawing a Circle 
        System.out.println(square.draw()); // Output: Drawing a Squ
    }


}
