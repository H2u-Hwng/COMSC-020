import java.util.Scanner; 

public class LeapYear {
	
	public static boolean isLeapYear(int year) {
		// Check whether the year is a leap year 
		return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
	}
	
	public static void main(String args[]) {
	    Scanner input = new Scanner(System.in); // Create a Scanner
	    
	    // Prompt the user for a year
	    System.out.print("Enter a year: ");
	    int year = input.nextInt();

	    // Display the result in a message dialog box
	    System.out.println(year + " is a leap year? " + isLeapYear(year));   
	} 
}
