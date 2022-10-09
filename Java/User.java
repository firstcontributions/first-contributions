import java.time.LocalDateTime;
public class User{
    protected int id;
    public String name;
    public int age;
    protected String username;
    protected String password;
    public Boolean enabled = true;

    static User[] userList= new User[5];
    static Book[] availableBooks=new  Book[10];
    static Transaction[] transactionList=new Transaction[50];

    //static variables to keep track of no of users,books and txs
    static int userCount = 0;
	static int bookCount = 0;
	static int transactionCount = 0;

    //constructor
    User(int id, String name,int age, String username, String password){
		this.id = id;
		this.name = name;
		this.age = age;
		this.username = username;
		this.password = password;

		userList[userCount] = this;//adding the new user to UserList
		userCount++;//increasing the count of users

	}
    Transaction tx;//local tx reference to store a newly generated tx
    LocalDateTime date;
    void addTransaction(int id, String details,  LocalDateTime dt){
		tx = new Transaction(id, details, date);
		transactionList[transactionCount] = tx;
		transactionCount++;
	}
    //authenticate method returns true if username and password matches else returns false
    static User authenticate(String username,String password){
        for (User i : userList) {
            if(i==null)//exception handling-nullpointer exception
				continue;
            if(i.username.equals(username) && i.password.equals(password) && i.enabled==true)
				return i;    
        }
        return null;
    }



}