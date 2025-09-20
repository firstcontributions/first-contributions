
public class AdapterPatternExample {

    interface Railroad {
        void vehiclemoving();
    }

    static class Car {
        public void drive() {
            System.out.println("Car is driving");
        }
    }
    static class Adapter implements Railroad {
        private final Car car;

        public Adapter(Car car) {
            this.car = car;
        }

        @Override
        public void vehiclemoving() {
            car.drive();
        }
    }

    public static void main(String[] args) {
        Car car = new Car();
        Railroad railroad = new Adapter(car);
        railroad.vehiclemoving();

    }
}
