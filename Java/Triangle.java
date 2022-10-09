import java.util.*;
public class Triangle {
 
    public static void main(String args[])
    {
    int a,b,c;
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter first side:");
    a=sc.nextInt();
    System.out.println("Enter second side:");
    b=sc.nextInt();
    System.out.println("Enter third side:");
    c=sc.nextInt();

    try
    {
        if(a+b>=c && b+c>=a && c+a>=b )
        {
          System.out.println("Triangle is Valid");
          int s=(a+b+c)/2;
          double area=s*(s-a)*(s-b)*(s-c);
          double res=Math.sqrt(area);
          System.out.println("Area:"+res);
        }
        else
        {
            System.out.println("Triangle is InValid");
            throw new InvalidTriangleException();
        }

    }
    catch (Exception e)
    {
     e.printStackTrace();
    }
 }
}
class InvalidTriangleException extends Exception{
    InvalidTriangleException(String str)
    {
        super(str);
    }

    public InvalidTriangleException() {
    }
}