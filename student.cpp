// give me a student class with getter setter and ctor
#include <string>
#include <iostream>
using namespace std;

class Student {
private:
    std::string name;
    int age;

public:
    // Constructor
    Student(std::string name, int age) {
        this->name = name;
        this->age = age;
    }

    // Getter for Name
    std::string getName() const {
        return name;
    }

    // Setter for Name
    void setName(std::string name) {
        this->name = name;
    }

    // Getter for Age
    int getAge() const {
        return age;
    }

    // Setter for Age
    void setAge(int age) {
        this->age = age;
    }
};
