import java.util.Scanner;

/**
 * Demonstrate input validation using if statements.
 */

public class Logarithm {
    
    public static void newLine() {
        System.out.println();
    }    
    
    public static void main(String[] args) {
        
        // prompt for input
        Scanner in = new Scanner(System.in);
        System.out.print("Enter a number: ");
        
        // check the format
        if (!in.hasNextDouble()) {
            String word = in.next();
            System.err.println(word + " is not a number");
            return;
        }
        
        // check the range
        double x = in.nextDouble();
        newLine(); // for readability
        if (x > 0) {
            double y = Math.log(x);
            System.out.printf("The log is %.2f", y);
        } else {
            System.out.println("The log is undefined");
        }
    }
} 
