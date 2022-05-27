import java.util.Scanner;
class StackOfIntegers {
	private int[] elements;
	private int size;
	public static final int DEFAULT_CAPACITY = 16;

	/** Construct a stack with the default capacity 16 */
	public StackOfIntegers() {
		this (DEFAULT_CAPACITY);
	}

	/** Construct a stack with the specified maximum capacity */
	public StackOfIntegers(int capacity) {
		elements = new int[capacity];
	}

	/** Push a new integer to the top of the stack */
	public void push(int value) {
		if (size >= elements.length) {
			int[] temp = new int[elements.length * 2];
			System.arraycopy(elements, 0, temp, 0, elements.length);
			elements = temp;
		}

		elements[size++] = value;
	}

	/** Return and remove the top element from the stack */
	public int pop() {
		return elements[--size];
	}

	/** Return the top element from the stack */
	public int peek() {
		return elements[size - 1];
	}

	/** Test whether the stack is empty */
	public boolean empty() {
		return size == 0;
	}

	/** Return the number of elements in the stack */
	public int getSize() {
		return size;
	}
}
public class Test {
	/** Main method */
	public static void main(String[] args) {
		// Create a Scanner
		Scanner input = new Scanner(System.in);

		// Prompt the user to enter a positive integer
		System.out.print("Enter a positive integer: ");
		int number = input.nextInt();

		// Displays all the number's smallest factors in decreasing order
		System.out.print("The smallest factors of " + number + " are: ");
		StackOfIntegers stack = new StackOfIntegers(); // Create a StackOfIntegers

		smallestFactors(number, stack);

		while (!stack.empty()) {
			System.out.print(stack.pop() + " ");
		}
		System.out.println();
	}

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
}










//try {
//	
//}
//catch (InputMismatchException ex) {
//	System.err.println("Please use digits only.");
//}
//catch (ArithmeticException ex) {
//	System.err.println("Division by zero is not allowed.");
//}
//catch (Exception ex) {
//	System.err.println("Error in program.");
//} 