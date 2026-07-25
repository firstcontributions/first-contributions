import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        if ( a % 13 == 0 || a % 19 == 0 ) {
            System.out.print("True");
        }
        else {
            System.out.print("False");
        }
    }
}