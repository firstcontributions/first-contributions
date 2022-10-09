import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;

class TimeZone{
    int day;
    int month;
    int year;
    int hh;
    int mm;
    int sec;
    String ap;
    TimeZone(int d,int m,int y,int h,int min,int s,String a){
        day=d;
        month=m;
        year=y;
        hh=h;
        mm=min;
        sec=s;
        ap=a;
    }
}
class Main {

    static String DATE_FORMAT = "dd-MM-yyyy hh:mm:ss a";

    public static void main(String[] args) {
        //Create your time class object
        TimeZone m1=new TimeZone(4,6,2022,10,15,55,"PM");
        
        //Add leading 0 if day and month is less than 10
        String d=Integer.toString(m1.day);
        String m=Integer.toString(m1.month);
        if(m1.day<10) 
            d="0"+m1.day;
        if(m1.month<10)
            m="0"+m1.month;
        
        //Declare the required Date format    
        String dateInString = d+"-"+m+"-"+m1.year+" "+m1.hh+":"+m1.mm+":"+m1.sec+" "+m1.ap;
        //String dateInString = "04-06-2022 10:15:55 AM";
        
        //Create LocalDateTime object
        LocalDateTime ldt = LocalDateTime.parse(dateInString, DateTimeFormatter.ofPattern(DATE_FORMAT));

        //Create a Zone Id
        ZoneId indiaZoneId = ZoneId.of("Asia/Kolkata");
        System.out.println("TimeZone : " + indiaZoneId);

        ZonedDateTime asiaZonedDateTime = ldt.atZone(indiaZoneId);
        System.out.println("Date (India) : " + asiaZonedDateTime);

        ZoneId newYokZoneId = ZoneId.of("America/New_York");
        System.out.println("TimeZone : " + newYokZoneId);

        ZonedDateTime nyDateTime = asiaZonedDateTime.withZoneSameInstant(newYokZoneId);
        System.out.println("Date (New York) : " + nyDateTime);

        DateTimeFormatter format = DateTimeFormatter.ofPattern(DATE_FORMAT);
        System.out.println("\n---DateTimeFormatter---");
        System.out.println("Date (India) : " + format.format(asiaZonedDateTime));
        System.out.println("Date (New York) : " + format.format(nyDateTime));

    }

}