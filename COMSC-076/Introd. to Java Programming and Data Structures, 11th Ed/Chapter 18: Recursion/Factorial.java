public class Factorial {
    
    public static void main(String[] args) {
        java.util.Scanner input = new java.util.Scanner(System.in);
        
        System.out.print("Enter a number: ");
        int n = input.nextInt();
        
        System.out.println("Factorial = " + factorial(n));
    }
    
    /** Return the factorial for a specified index */
    public static long factorial(int n) {
        if (n == 0) // Base case
            return 1;
        else
            return n * factorial(n - 1); // Recursive call
    }
}
