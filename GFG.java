
public class GFG {

    static class Singleton {

        private static Singleton ins = null;

        private Singleton() {
        }

        public static Singleton getInstance() {
            if (ins == null) {
                ins = new Singleton();
            }
            return ins;
        }
    }

    public static void main(String args[]) {
        Singleton x = Singleton.getInstance();
        Singleton y = Singleton.getInstance();
        Singleton z = Singleton.getInstance();

        System.out.println("Hashcode of x is " + x.hashCode());
        System.out.println("Hashcode of y is " + y.hashCode());
        System.out.println("Hashcode of z is " + z.hashCode());

        if (x == y && y == z) {
            System.out.println("Three objects point to the same memory location on the heap i.e, to the same object");
        } else {
            System.out.println("Three objects DO NOT point to the same memory location on the heap");
        }
    }

}
