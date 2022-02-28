public class PrintTime {

    public static void printTime(int hour, int minute) {
        System.out.printf("%02d:%02d\n", hour, minute);
    }
  
    public static void main(String[] args) {
        int hour = 11;
        int minute = 59;
        
        printTime(hour, minute);
        printTime(hour + 1, 0);
    }
}
