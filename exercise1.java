import java.util.Scanner;

/**
 * Prompts the user for 3 edges of a triangle. 
 * Computes the perimeter if the input is valid or 
 * displays the input is invalid otherwise.
 */

public class exercise1 {
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		// prompt for 3 edges of a triangle
		System.out.print("Enter the first edge: ");
		double edge1 = input.nextDouble();
		
		System.out.print("Enter the second edge: ");
		double edge2 = input.nextDouble();
		
		System.out.print("Enter the third edge: ");
		double edge3 = input.nextDouble();
		
		// check whether the input is valid
		if ((edge1 + edge2) > edge3 
		 && (edge2 + edge3) > edge1
		 && (edge3 + edge1) > edge2) {	
			
			// calculate and display the perimeter
			double perimeter = edge1 + edge2 + edge3;
			System.out.println("Perimeter = " + perimeter);
			
		} else {
			System.out.println("The input is invalid.");
		}
	}
}
