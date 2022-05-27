import java.util.Scanner;
import java.util.InputMismatchException;

public class Sum {
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		int n1 = 0;
		int n2 = 0;
		
		boolean valid = false;
		while (!valid) {
			try {
				System.out.print("Enter two integers (separated by a space): ");
				n1 = input.nextInt();
				n2 = input.nextInt();
				
				valid = true;
			}
			catch (InputMismatchException ex) {
				input.nextLine();
				System.out.println("Please use integers only.");
			}
			catch (Exception ex) {
				System.out.println("Error in program.");
			}
		} 
		
		System.out.printf("Sum = %d", n1 + n2);
	}
}
