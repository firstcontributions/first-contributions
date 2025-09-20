public class ProxyPatternDemo {
    interface Image {
        void display();
    }

    public static class RealImage implements Image {
        private final String fileName;

        public RealImage(String fileName) {
            this.fileName = fileName;
            loadFromDisk(fileName);
        }

        private void loadFromDisk(String fileName) {
            System.out.println("Loading " + fileName);
        }

        @Override
        public void display() {
            System.out.println("Displaying " + fileName);
        }
    }

    public static class ProxyImage implements Image {
        private final String fileName;
        private RealImage realImage;

        public ProxyImage(String fileName) {
            this.fileName = fileName;
        }

        @Override
        public void display() {
            if (realImage == null) {
                realImage = new RealImage(fileName);
            }
            realImage.display();
        }
    }


    public static void main(String[] args) {
        Image image = new ProxyImage("test_image.jpg");

        // Image will be loaded from disk
        image.display();
        System.out.println("");

        // Image will not be loaded from disk
        image.display();
    }
    
}
