import java.util.*;

public class Test {
	
	
	public static void main(String[] args) {
		HashMap<String, Double> dictionary = new HashMap<String, Double>();
		dictionary.put("mowing", 100.0);
		dictionary.put("tree removal", 1000.0);
		dictionary.put("planting", 300.0);
		
		Scanner input = new Scanner(System.in);
	
		System.out.println("Services: mowing, tree removal, and planting.");
		
		System.out.print("How many services you want to choose? ");
		
		while (!input.hasNextInt()) {
			System.err.print("ERROR! " + input.nextLine() + " is not a number.");
			System.out.println();
			
			System.out.print("\nEnter an integer number: ");
		}
		
		int number = input.nextInt();
		
		String[] servicesList = new String[number];
		
		double money;
		double totalCost = 0.0;
		String service = "";
		for (int i = 0; i < number; i++ ) {
			String work = input.nextLine().toLowerCase();
			System.out.printf("%d. Type the service you want: %s", i + 1);
			//String work = input.nextLine().toLowerCase();//.replaceAll("\\s", "");
		}
		// Get the iterator over the HashMap
        Iterator<Map.Entry<String, Double>> iterator = dictionary.entrySet().iterator();
		
		for (int i = 0; i < number; i ++) {
			boolean isKeyPresent = false;
			
			
			while (! isKeyPresent) {
				System.out.printf("%d. Type the service you want: ", i + 1);
				service = input.nextLine().toLowerCase();//.replaceAll("\\s", "");
				
				isKeyPresent = dictionary.containsKey(service);
			} 
			
			money = dictionary.get(service);
			servicesList[i] = service;
			totalCost += money;
			System.out.printf("Its base charge is $%,.2f. \n", money);
		} 
		
		System.out.println("Services you chose are " + Arrays.toString(servicesList));
		System.out.println("Total cost: $" + totalCost);
			
			 
			
			
	            
//				System.out.printf("%d. Type the service you want: ", i + 1);
//				String service = input.nextLine().toLowerCase();//.replaceAll("\\s", "");
//				if (dictionary.get(service) != null) {
//					double money = dictionary.get(service);
//					System.out.printf("Its base charge is $%,.2f. \n", money);

//					isValid = true;
//					
//				} else { 
//					System.err.println("ERROR! Please enter the valid service. \n");
//				}
//				
//			
//			
//		
//		

//			
////			switch(service) {

//		
//		System.out.println(totalCost);
	}
}

