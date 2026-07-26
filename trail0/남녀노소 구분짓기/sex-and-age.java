import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int gender = sc.nextInt();
        int age = sc.nextInt();
        if ( gender == 0) {
            if ( age >= 19) {
                System.out.print("MAN");
            }
            else {
                System.out.print("BOY");
            }
            }
        else if (gender == 1 ) {
             if ( age >= 19) {
                System.out.print("WOMAN");
            }
            else {
                System.out.print("GIRL");
            }
        }
        }

    }
