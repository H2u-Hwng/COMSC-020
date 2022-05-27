import java.util.Scanner;
import java.util.InputMismatchException;
import java.util.ArrayList;
import java.util.List;

public class SmallestFactors {
    /** Main method */
    public static void main(String[] args) {
        // Create a Scanner
        Scanner input = new Scanner(System.in);
        
        // Prompt the user to enter a positive integer
        boolean valid = false;
        int number = 0;
        
        while (!valid) {
            try {
                System.out.print("Enter a positive integer: ");
                number = input.nextInt();
                if (number > 0) {
                    valid = true;
                } else {
                    System.out.println("The number must be greater than zero.");
                }
            } 
            catch (InputMismatchException ex) {
                input.nextLine();
                System.out.println("Please use integers only.");
            }
            catch (Exception ex) {
                System.out.println("Error in program.");
            }
        }
        
        // Find smallest factors and add them to myList
        int prime = 2; // Potential prime factor
        
        List<Integer> myList = new ArrayList<>();
        
        while (number / prime != 1) {
            if (number % prime == 0) {
                myList.add(prime);
                number /= prime;
            } else {
                prime++;
            }
        }
        myList.add(number);
        
        // Displays all the number's smallest factors in decreasing order
        System.out.println("All its smallest factors in decreasing order:");
        for (int i = myList.size() - 1; i > -1; i--) {
            System.out.printf("%d ", myList.get(i));
        }
    }
}