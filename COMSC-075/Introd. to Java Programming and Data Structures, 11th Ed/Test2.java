
import java.util.*;

public class Test2 {
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		System.out.println("Services: mowing, tree removal, and planting.");
		
		System.out.print("How many services you want to choose? ");
		
		while (!input.hasNextInt()) {
			System.err.println("ERROR! " + input.nextLine() + " is not a number.");
			System.out.println();
			
			System.out.print("Enter an integer number: ");
		}
		
		int number = input.nextInt();
		
		String[] servicesList = new String[number];
		
		boolean isValid = false;
		double money = 0;
		double totalCost = 0.0;
		String service = "";
		
		for (int i = 0; i < number; i ++) {
			while (! isValid) {
				System.out.print(i + 1 + ". Type the service you want: ");
				service = input.nextLine().toLowerCase();
				
				if (service == "mowing") money = 100.0; 
				else if (service == "tree removal") money = 1000.0;
				else if (service == "planting") money = 300.0;
				else:
				
				default:
					System.out.println("Enter valid.");
				}
				servicesList[i] = service;
				totalCost += money;
				isValid = true;
			}
			
		}
		
		System.out.println("Services you chose are " + Arrays.toString(servicesList));
		System.out.println("Total cost: $" + totalCost);
		
	}
}
