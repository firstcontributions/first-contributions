import java.util.Timer;
import java.util.TimerTask;
import java.text.SimpleDateFormat;
import java.util.Date;

public class AlarmClock {

    public static void main(String[] args) {
        // Set the alarm time (24-hour format)
        String alarmTime = "15:30"; // Change this to your desired alarm time

        // Create a timer
        Timer timer = new Timer();

        // Define a task to be executed when the alarm time is reached
        TimerTask task = new TimerTask() {
            public void run() {
                SimpleDateFormat sdf = new SimpleDateFormat("HH:mm");
                String currentTime = sdf.format(new Date());
                if (currentTime.equals(alarmTime)) {
                    System.out.println("Alarm! It's time to wake up!");
                    // You can replace the message with any action you want
                }
            }
        };