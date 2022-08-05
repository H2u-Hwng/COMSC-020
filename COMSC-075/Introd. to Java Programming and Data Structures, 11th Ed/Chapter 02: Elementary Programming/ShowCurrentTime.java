public class ShowCurrentTime {
    public static void main(String[] args) {
        // Obtain the total milliseconds
        long totalMilliseconds = System.currentTimeMillis();
        
        // Compute the total seconds
        long totalSeconds = totalMilliseconds / 1000;
        
        // Compute the total minutes and current second
        long totalMinutes = totalSeconds / 60;
        long currentSecond = totalSeconds % 60;
        
        // Compute the total hours and current minute
        long totalHours = totalMinutes / 60;
        long currentMinute = totalMinutes % 60;
        
        // Compute the current hour
        long currentHour = totalHours % 24;
        
        // Disply the current time
        System.out.printf("The current time is %02d:%02d:%02d GMT", 
                          currentHour, currentMinute, currentSecond);
    }
}
