import java.util.Scanner;

/**
 * Prompts the user for pounds 
 * Converts pounds to kilograms and displays the result.
 */

public class HuuHungNguyenLab01b {

	public static void main(String[] args) {
		
		// constant
		final double LB_TO_KG = 0.454; 
		
		Scanner input = new Scanner(System.in);
		
		System.out.print("Enter a number in pounds: ");
		double pounds = input.nextDouble(); // prompt for pounds
		
		// calculate and display the kilograms
		double kilograms = pounds * LB_TO_KG;
		System.out.printf("%.3f lbs is %.3f kg.", pounds, kilograms);
	}
}
