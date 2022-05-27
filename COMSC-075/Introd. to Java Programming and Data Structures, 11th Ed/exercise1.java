import java.util.Scanner;

public class exercise1 {
	
	/** Find smallestFactors and push them to StackOfIntegers */
	public static void smallestFactors(int number, StackOfIntegers stack) {
		int i = 2; // Potential prime factor
		while (number / i != 1){ 
			if (number % i == 0) {
				stack.push(i);
				number /= i;
			}
			else
				i++;
		}
		stack.push(number);
	}
	
	/** Main method */
	public static void main(String[] args) {
		// Create a Scanner
		Scanner input = new Scanner(System.in);

		// Prompt the user to enter a positive integer
		System.out.print("Enter a positive integer: ");
		
		
		
		
		int number = 0;
		
		boolean valid = false;
		while (!valid) {
			while (!input.hasNextInt()) {
				String word = input.nextLine();
				System.err.println(word + " is not a positive integer!");
			}
			
			number = input.nextInt();
			if (number <= 0) {
				System.err.println(number + " is not a positive integer!");
			} else {
				valid = true;
			}
			
			if (number == 0) break;
		}
		
		// Displays all the number's smallest factors in decreasing order
		System.out.print("The smallest factors of " + number + " are: ");
		StackOfIntegers stack = new StackOfIntegers(); // Create a StackOfIntegers

		smallestFactors(number, stack);

		while (!stack.empty()) {
			System.out.print(stack.pop() + " ");
		}
		System.out.println();
	}

	
}