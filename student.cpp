// give me a student class with getter setter and ctor
public class Student {
    private String name;
    private int age;

    // Constructor
    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Getter for Name
    public String getName() {
        return name;
    }

    // Setter for Name
    public void setName(String name) {
        this.name = name;
    }

    // Getter for Age
    public int getAge() {
        return age;
    }

    // Setter for Age
    public void setAge(int age) {
        this.age = age;
    }
}