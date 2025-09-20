
public class FactoryPatternDemo {

    static public interface Shape {
        void draw();
    }

    static public class Rectangle implements Shape {

        @Override
        public void draw() {
            System.out.println("Inside Rectangle::draw() method.");
        }
    }

    static public class Square implements Shape {

        @Override
        public void draw() {
            System.out.println("Inside Square::draw() method.");
        }
    }

    static public class Circle implements Shape {

        @Override
        public void draw() {
            System.out.println("Inside Circle::draw() method.");
        }
    }

    static public class ShapeFactory{
        public Shape getShape(String shapeType){
            if(shapeType == null){
                return null;
            }
            if(shapeType.equalsIgnoreCase("CIRCLE")){
                return new Circle();
            } else if(shapeType.equalsIgnoreCase("RECTANGLE")){
                return new Rectangle();
            } else if(shapeType.equalsIgnoreCase("SQUARE")){
                return new Square();
            }
            return null;
        }
    }

    public static void main(String[] args) {
        ShapeFactory shapeFactory = new ShapeFactory();

        // Get an object of Circle and call its draw method
        Shape shape1 = shapeFactory.getShape("CIRCLE");
        shape1.draw();

        // Get an object of Rectangle and call its draw method
        Shape shape2 = shapeFactory.getShape("RECTANGLE");
        shape2.draw();

        // Get an object of Square and call its draw method
        Shape shape3 = shapeFactory.getShape("SQUARE");
        shape3.draw();
    }

}
