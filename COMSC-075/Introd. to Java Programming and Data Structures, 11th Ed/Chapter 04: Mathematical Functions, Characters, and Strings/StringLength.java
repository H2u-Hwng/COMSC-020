import java.util.Scanner;

public class StringLength {
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a string: ");
        String sentence = input.nextLine();

        System.out.printf("The string if of length %d and the first character is %s.\n", 
                            sentence.length(), sentence.charAt(0));
    }
}
