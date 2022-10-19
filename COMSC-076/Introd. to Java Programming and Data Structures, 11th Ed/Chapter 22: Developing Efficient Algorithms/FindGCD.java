import java.util.Scanner;

public class FindGCD {
    /** Main method*/
    public static void main(String[] args) {
        // Create a scanner
        Scanner input = new Scanner(System.in);
        
        // Prompt the user for 2 integers 
        System.out.print("Enter 2 integers split by a space: ");
        int m = input.nextInt();
        int n = input.nextInt();
        
        System.out.println("GCD = " + GCD(m, n));
    }
    
    /** Find gcd for intergers m and n */
    public static int GCD(int m, int n) {
        if (m % n == 0) { // Base case
            return n;
        } else {
            return GCD(n, m % n);
        }
    }
}
