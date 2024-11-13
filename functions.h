//functions
void iphone(int);
void macbook(int);
void ipad(int);
void airpods(int);
void watch(int);
void cart_summary();
void phone_email();
void payment();
void cash_memo();


//variables
int loop = 1; 
int yesno;
int x = 0;
int sum;
int i;
char phone[10];
char email[25];
char email_verification[1] = "@";
char *p;
//payment global variables
int cash, pay_method;
char credit[16];
int credit_verify;
int ex_month, ex_year, year = 22, month = 01;
char cardholder_name[40];
char CVV[3];
int OTP;
char UPI[25], UPI_verification[] = "@upi", upi_passcode[6];

//bill global variables
char name[10];
char *paid_by;