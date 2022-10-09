import java.time.LocalDateTime;

class Transaction{
	int id;
	String details;
	LocalDateTime date;

	Transaction(int id, String details, LocalDateTime date){
		this.id = id;
		this.details = details;
		this.date = date;
	}

	void displayTransaction(){
		System.out.println("Transaction id: "+id+"/ details: "+details+"/ date: "+date);
	}
}