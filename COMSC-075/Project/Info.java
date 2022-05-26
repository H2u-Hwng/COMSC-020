import java.util.InputMismatchException;
import java.util.Scanner;

public class Info {
	
	private int baseZipCodeCost;
	
	public Info() {
		
		Scanner input = new Scanner(System.in);
		
		System.out.println("First name (Required): ");
		String firstName = input.nextLine(); 
		
		System.out.println("Last name (Required): ");
		String lastName = input.nextLine(); 

		System.out.println("Email (Required): ");
		String email = input.nextLine(); 

		System.out.println("Phone number (Required): ");
		String phoneNumber = input.nextLine(); 
	}
	
	public double getZipCodeCost() {
		
		boolean valid = false;
		int zipCode = 0;
		
		while (!valid) {
			try {
				Scanner input = new Scanner(System.in);
				System.out.print("Zip code (Required): ");
				 zipCode = input.nextInt(); 
				
				if (zipCode >= 95110 && zipCode <= 95139) {
					valid = true;
					
					if (zipCode <= 95120) {
						baseZipCodeCost = 150;
				        System.out.println("The base cost in your area is: $" + baseZipCodeCost + "\n");
					} else if (zipCode <= 95129) {
						baseZipCodeCost = 200;
				        System.out.println("The base cost in your area is: $" + baseZipCodeCost + "\n");
					} else {
						baseZipCodeCost = 400;
						System.out.println("The base cost in your area is: $" + baseZipCodeCost + "\n");
					}
				} else {
					System.err.println("Invalid zipcode, please try again.");
				}
			} catch (InputMismatchException ex) {
				System.err.println("Please use digits only.");
			} catch (Exception ex) {
				System.err.println("Error in program.");
			}
		}
		
		return baseZipCodeCost;
	}
}