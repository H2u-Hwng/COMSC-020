import java.util.Scanner;
import java.util.InputMismatchException;

public class exercise2 {
	
	public static void main(String[] args) {
		int n1 = 0;
		int n2 = 0;
		
		boolean valid = false;
		while (!valid) {
			try {
				Scanner input = new Scanner(System.in);
				System.out.print("Enter two integers (separated by a space): ");
				n1 = input.nextInt();
				n2 = input.nextInt();
				
				valid = true;
			}
			catch (InputMismatchException ex) {
				System.err.println("Please use integers only.");
			}
			catch (Exception ex) {
				System.err.println("Error in program.");
			}
		} 
		
		System.out.printf("sum = %d", n1 + n2);
	}
}
