import java.util.Scanner;

public class PrintTime {
    
    public static void newLine() {
        System.out.println();
    }
    
    // display the time
    public static void printTime(int hour, int minute) {
        System.out.printf("%02d:%02d", hour, minute);
        newLine();
    }
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        // prompt the user for a hour
        System.out.print("Enter a hour: ");
        int hour = in.nextInt();
        
        newLine(); // for readability
        
        // prompt the user for a minute
        System.out.print("Enter a minute: ");
        int minute = in.nextInt();
        
        newLine(); // for readability
        
        printTime(hour, minute); // display the time
        printTime(hour + 1, minute); // display the time after an hour
    }
}
