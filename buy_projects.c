#include<stdio.h>
#include<string.h>
#include"structure.h"
#include"functions.h"
int main()
{
    int choice, interest;

    printf("Hello! Welcome to Apple store! Kindly enter your name below:\n");
    // gets(name);
    scanf("%s", &name);
    
    while(loop)
    {
        printf("Dear %s, select the product you are interested in:\n", name);

        printf("1. iPhone\n2. MacBook\n3. iPad\n4. AirPods\n5. Apple Watch\n");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1: 
                printf("Which iPhone are you interested in?\nWe have the following available:\n");
                for(i = 0; i <= 3; i++)
                    printf("%d. %s\n", i + 1, iPhone[i].name);
                printf("Enter the serial number:\n");
                scanf("%d", &interest);
                interest--;
                iphone(interest);
                break;
            
            case 2: 
                printf("Which MacBook are you interested in?\nWe have the following available:\n");
                for(i = 0; i <= 3; i++)
                    printf("%d. %s\n", i + 1, MacBook[i].name);
                printf("Enter the serial number:\n");
                scanf("%d", &interest);
                interest--;
                macbook(interest);
                break;
            
            case 3: 
                printf("Which iPad are you interested in?\nWe have the following available:\n");
                for(i = 0; i <= 3; i++)
                    printf("%d. %s\n", i + 1, iPad[i].name);
                printf("Enter the serial number:\n");
                scanf("%d", &interest);
                interest--;
                ipad(interest);
                break;

            case 4: 
                printf("Which AirPods are you interested in?\nWe have the following available:\n");
                for(i = 0; i <= 3; i++)
                    printf("%d. %s\n", i + 1, AirPods[i].name);
                printf("Enter the serial number:\n");
                scanf("%d", &interest);
                interest--;
                airpods(interest);
                break;

            case 5: 
                printf("Which Apple Watch are you interested in?\nWe have the following available:\n");
                for(i = 0; i <= 2; i++)
                    printf("%d. %s\n", i + 1, Watch[i].name);
                printf("Enter the serial number:\n");
                scanf("%d", &interest);
                interest--;
                watch(interest);
                break;

            default:
                printf("Out of order!\n");
        }
    }
    if(x > 0)
    {

        cart_summary();

        phone_email();
        
        payment();

        cash_memo();
    }

    return 0;
}

void iphone(int model)
{
    printf("Details of %s are:\n", iPhone[model].name);
    printf("Specs = %s\nPrice = Rs. %d\n\n", iPhone[model].specs, iPhone[model].price);

    //cart 

    printf("Do you want to purchase %s(yes = 1 / no = 0)?\n", iPhone[model].name);
    scanf("%d", &yesno);

    if(yesno == 1)
    {
        cart[x] = iPhone[model];
        printf("Great! %s has been added to your cart.\n", cart[x].name);
        x++;
        //printf("Do you want to view your cart?")
    }

    printf("Do you want to add another item(yes = 1 / no = 0)?\n");
    scanf("%d", &loop);
}

void macbook(int model)
{
    printf("Details of %s are:\n", MacBook[model].name);
    printf("Specs = %s\nPrice = Rs. %d\n\n", MacBook[model].specs, MacBook[model].price);

    //cart 

    printf("Do you want to purchase %s(yes = 1 / no = 0)?\n", MacBook[model].name);
    scanf("%d", &yesno);

    if(yesno == 1)
    {
        cart[x] = MacBook[model];
        printf("Great! %s has been added to your cart.", cart[x].name);
        x++;
        //printf("Do you want to view your cart?")
    }

    printf("Do you want to add another item(yes = 1 / no = 0)?\n");
    scanf("%d", &loop);
}

void ipad(int model)
{
    printf("Details of %s are:\n", iPad[model].name);
    printf("Specs = %s\nPrice = Rs. %d\n\n", iPad[model].specs, iPad[model].price);

    //cart 

    printf("Do you want to purchase %s(yes = 1 / no = 0)?\n", iPad[model].name);
    scanf("%d", &yesno);

    if(yesno == 1)
    {
        cart[x] = iPad[model];
        printf("Great! %s has been added to your cart.", cart[x].name);
        x++;
        //printf("Do you want to view your cart?")
    }

    printf("Do you want to add another item(yes = 1 / no = 0)?\n");
    scanf("%d", &loop);
}

void airpods(int model)
{
    printf("Details of %s are:\n", AirPods[model].name);
    printf("Specs = %s\nPrice = Rs. %d\n\n", AirPods[model].specs, AirPods[model].price);

    //cart 

    printf("Do you want to purchase %s(yes = 1 / no = 0)?\n", AirPods[model].name);
    scanf("%d", &yesno);

    if(yesno == 1)
    {
        cart[x] = AirPods[model];
        printf("Great! %s has been added to your cart.", cart[x].name);
        x++;
        //printf("Do you want to view your cart?")
    }

    printf("Do you want to add another item(yes = 1 / no = 0)?\n");
    scanf("%d", &loop);
}

void watch(int model)
{
    printf("Details of %s are:\n", Watch[model].name);
    printf("Specs = %s\nPrice = Rs. %d\n\n", Watch[model].specs, Watch[model].price);

    //cart 

    printf("Do you want to purchase %s(yes = 1 / no = 0)?\n", Watch[model].name);
    scanf("%d", &yesno);

    if(yesno == 1)
    {
        cart[x] = Watch[model];
        printf("Great! %s has been added to your cart.", cart[x].name);
        x++;
        //printf("Do you want to view your cart?")
    }

    printf("Do you want to add another item(yes = 1 / no = 0)?\n");
    scanf("%d", &loop);
}

void cart_summary(){
    printf("Here is your cart total:\n");
    printf("Items:\n");
    for(i = 0; i < x; i++)
        printf("%d. %s - %d\n", i + 1, cart[i].name, cart[i].price);
        
    printf("And your total bill is:\n");
    for(i = 0; i < x; i++)
        sum = sum + cart[i].price;

    printf("Rs. %d\n\n", sum);
};

void phone_email()
{
    printf("Enter your phone number:\n");
    scanf("%s", phone);
    while(strlen(phone) != 10)
    {
        printf("Invalid Number! Enter number again:\n");
        scanf("%s", phone);
    };

    printf("Enter your email address:\n");
    scanf("%s", email);
    p = strstr(email, email_verification);
    if(p)
        ;
    else
    {
        printf("Invalid email! Enter email again:\n");
        scanf("%s", email);
    }

}

void payment()
{
    printf("How would you like to pay your bill?\n");
    printf("1. Cash\n2. Card\n3. UPI/BHIM\n");
    scanf("%d", &pay_method);
        
    switch(pay_method)
    {
        case 1: 
            printf("Your bill is Rs. %d\n", sum);
            printf("Enter the cash you paid:\n");
            scanf("%d", &cash);
            if(cash > sum)
                printf("Here is your change of Rs. %d", cash - sum);
                int sum_cash = sum;
            while(sum > cash)
            {
                sum_cash = sum_cash - cash;
                printf("Insufficient cash! Please pay the remaining amount of Rs. %d", sum_cash);
                scanf("%d", &cash);
                if(cash > sum_cash)
                    printf("Here is your change of Rs. %d", cash - sum);
            }
            paid_by = "Cash";
            break;

        case 2:
            printf("Your bill is Rs. %d\n", sum);
            printf("Enter the cardholder's name:\n");
            scanf("%s", cardholder_name);

            printf("Enter your Credit/Debit card number(16 digits):\n");
            scanf("%s", credit);

            credit_verify = strlen(credit);

            while(credit_verify != 16)
            {
                printf("Invalid Credit Card Number! Enter a 16 digit credit card number:\n");
                scanf("%s", credit);

                credit_verify = strlen(credit);
            }

            printf("Enter your Expiry date in the following format(MM,YY):\n");
            scanf("%d %d", &ex_month, &ex_year);
            if(ex_year > year || ex_month > month && ex_year >= year)
                ;
            else{
                printf("Your card has been expired! please try another payment method!\n");
                payment();
                break;
            }

            printf("Enter your CVV(3 digits):\n");
            scanf("%s", CVV);
            while(strlen(CVV) != 3)
            {
                printf("Invalid CVV! Enter a 3 digit CVV again:\n");
                scanf("%s", CVV);
                }

            printf("OTP has been sent.\n");
            printf("\t\t\tOTP = 123456\nEnter OTP:\n");
            scanf("%d", &OTP);
            if(OTP != 123456)
            {
                printf("Incorrect OTP. Please go through the payment process again.\n");
                payment();
            }
            paid_by = "Card";
            break;

        case 3: 
            printf("Your bill is %d\n", sum);
            printf("Enter your UPI id:\n");
            scanf("%s", UPI);
            p = strstr(UPI, UPI_verification);
            if(p)
                ;
            else
            {
                printf("Invalid ID. Please enter your ID again.\n");
                scanf("%s", UPI);
            }
            printf("Enter your 6 digit UPI passcode:\n");
            scanf("%s", upi_passcode);
            i = 1;
            while(strlen(upi_passcode) != 6)
            {
                printf("Incorrect passcode! %d failed attempts", i);
                scanf("%s", upi_passcode);
                i++;
            }
            paid_by = "UPI/BHIM";
            break;

            default:
                printf("Out of order!\n");
        }
}

void cash_memo()
{
    printf("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n");
    printf("Apple Cash Memo:\n");
    printf("  Cupertino, California, United States\n");
    printf("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n");
    printf("Customer Name: %s\n", name);
    printf("Mobile: %s\n", phone);
    printf("Email: %s\n", email);

    printf("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n");

    printf("Bill Summary:\n");
    for(i = 0; i < x; i++)
        printf("%d. %s - Rs.%d\n", i + 1, cart[i].name, cart[i].price);
        
    printf("\nTotal Sum: Rs. %d\n", sum);
    printf("THANK YOU FOR SHOPPING WITH US.\nHAVE A NICE DAY!\n");
    printf("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n");
    printf("Bill paid by %s\n", paid_by);
    printf("\n.");
}