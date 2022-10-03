#include <iostream>
#include <sstream>
using namespace std;

/*
Enter code for class Student here.
Read statement for specification.
*/
class Student
{
    private:
    int age, standard;
    string first_name, last_name;
  public:
  void set_age(int);
  void set_standard(int);
  void set_first_name(string);
  void set_last_name(string); 
  int get_age();
  int get_standard(void);
  string get_first_name(void);
  string get_last_name(void); 
  void to_string();
};
void Student::set_age(int a)
{
    age=a;
}
void Student::set_standard(int b)
{
    standard=b;
}
void Student::set_first_name(string c)
{
    first_name=c;
}
void Student::set_last_name(string d)
{
    last_name=d;
}
int Student::get_age()
{
    return age;
}
  int Student::get_standard()
  {
      return standard;
  }
  string Student::get_first_name()
  {
     return first_name;
  }
  string Student::get_last_name()
  {
      return last_name;
  }
  void Student::to_string()
  {
      cout<<age<<","<<first_name<<","<<last_name<<","<<standard;
  }
int main() {
    int age, standard;
    string first_name, last_name;
    
    cin >> age >> first_name >> last_name >> standard;
    
    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);
    
    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    st.to_string();
    
    return 0;
}
