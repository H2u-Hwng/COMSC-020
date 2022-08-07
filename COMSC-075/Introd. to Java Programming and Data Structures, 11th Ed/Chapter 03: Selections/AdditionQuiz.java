import java.util.Random;
import java.util.Scanner;

public class AdditionQuiz {
    public static void main(String[] args) {
        // create instance of Random class
        Random rand = new Random();
      
        // Generate random integers in range 0 to 99
        int randInt1 = rand.nextInt(100);
        int randInt2 = rand.nextInt(100);
        
        // Create a scanner
        Scanner input = new Scanner(System.in);
        
        // Prompt the user for an answer
        System.out.print(
          "What is " + randInt1 + " + " + randInt2 + "? ");
        int answer = input.nextInt();
      
        // Display the result
        System.out.printf("%d + %d = %d is %b. \n", 
                          randInt1, randInt2, answer, randInt1 + randInt2 == answer);
    }
}
