import java.util.Scanner;

public class Loop2 {
    
    public static void newLine() {
        System.out.println();
    }
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter a number: ");
      
        int number = in.nextInt(); // prompt the user for a number
        
        newLine(); // for readability
        
        while (number <= 8) {
            System.out.print(number + ", ");
            number += 2; // add 2 to number
        }
        System.out.println("Who do we appreciate?");
    }
}
