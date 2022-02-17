import java.util.Scanner;

/**
 * Prompts the user for a three-digit integer.
 * Determines whether it is a palindrome number.
 */

public class exercise2 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		System.out.print("Enter a three-digit integer: ");
		int number = input.nextInt(); // prompt for a three-digit integer
		
		int firstDigit = number / 100; // determine the first digit 
		
		int lastDigit = number % 10; // determine the last digit
		
		// check whether it is a palindrome number
		if (firstDigit == lastDigit) {
			System.out.println(number + " is a palindrome number.");
		} else {
			System.out.println(number + " isn't a palindrome number.");
		}
	}
}
