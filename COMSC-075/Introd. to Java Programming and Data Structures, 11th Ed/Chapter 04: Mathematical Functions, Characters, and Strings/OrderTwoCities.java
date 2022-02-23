import java.util.Scanner;

public class OrderTwoCities {
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		    
		// Prompt the user to enter two cities
		System.out.print("Enter the first city: ");
		String city1 = input.nextLine();
		
		System.out.print("Enter the second city: ");
		String city2 = input.nextLine();
		
		// Compare two cities and display them in alphabetical order
		if (city1.compareTo(city2) < 0)
			System.out.printf("The cities in alphabetical order are %s, %s.", city1, city2);
		else
			System.out.printf("The cities in alphabetical order are %s, %s.", city2, city1);
	}
}
