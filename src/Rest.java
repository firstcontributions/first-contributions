//How a normal java class become a part of REST API using Spring Boot
/*
What is an API?
API - Application Programming Interface
It allows two software to communicate with each other

Example: A frontend send request for the list of Students -> Backend respond with the list of Students
 */

/*
What is REST API?
REST- Representational State Transfer
REST is an architectural style used to build web services.
A REST API commonly uses HTTP Methods:
GET -> Read Data
POST -> Create data
PUT -> Replace or Update Data
PATCH -> Partially update data
Delete -> delete data

Examples:
GET     /apiname/students -> get all students
GET     /apiname/students/1 -> get student with id 1
POST    /apiname/students   -> create student
PUT     /apiname/students/1  -> update a student whose id is 1
DELETE  /apiname/students/1  -> delete a student whose id is 1
 */

/*
Can a Normal Java Class Become a REST API?
no, a plain java class does not:
- start an HTTP server
- receive HTTP request
- map URLs to Java method
- convert java objects into json
for these features we use spring boot
spring boot is a java language framework which handles all the object creation, api handling and let programmers focus only on business logic

 */

// A typical springboot class to create REST API
import org.springframework.web.bind.annotation.*; // we are importing a package from spring framework so that we can use it's annotations
import org.springframwork.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;//
@RestController //marks this class as controller, its methods return response data, commonly json(think like a language)
@RequestMapping("api/students") //map students table with this class (learn more about table in relational database
class RestController{

    //GET   /api/students
    @GetMapping("/{id}") //@GetMapping handles http get request and will return student with id which we will give input
    public String getAllStudents(){
        return "Rahul, Saumya, Divya, Rohit, Payal";
    }

    //Get   /api/students/10
    @GetMapping("/{id}")
    public String getStudentById(@PathVariable int id){ //@PathVariable reads a value from url path
        return "StudentId, name, section" +id;
    }

    //POST   /api/students
    @PostMapping //@PostMapping handles HTTP POST request
    public String createStudent(@RequestBody String Student){ // RequestBody reads a request body from json into a java object
        return "Recieved students: "+Student;
    }

    //DELETE  /api/stdudents/10
    @DeleteMapping("/{id") //@Delete mapping handles HTTP DELETE method
    public String deleteStudent(@PathVarible int id){
        return "Deleted student id"+id;
    }
}

/*
How Does a request work?
step1: A client(our browser-chrome) sends http request
step2: Spring Boot receives the request
step3: Spring maps the url and http method to a controller(eg GET method maps with @GetMapping
step4: The controller method executes(eg: getStudentById(@PathVariable int id) -> will return 10
step5: Spring Boot converts the returned value into a http response, language is json
step6: The client(browser-chrome) recieves the response - and we see the student id 10 on screen
 */

/*
How to test an api?
To work with api we can use such tools:
- Postman
- curl
- Swagger UI
 */

/*
Example of a rest API
REQUEST
Get http://localhost:8080/api/students

RESPONSE
"List of students"
 */

/*
What should we learn next?
- Return java object instead of strings
- Create a Student model class
- Use @ResponseEntity for http status code
- Validate incoming request data
- Connect a database using Spring Data Jpa
- Write test using JUnit and Mockito
 */

//main class: starts the spring boot application
@SpringBootApplication // tells spring boot that this is main application class and enables application configuration and componenet scanning
public class Rest{
    public static void main(String[]args){
        SpringApplication.run(Rest.class,args);// starts the spring application, initializes it's components, and starts embedded web server when required
    }
}
