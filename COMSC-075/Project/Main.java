import java.util.Scanner;

public class Main {
	
    public static void main(String[] args) throws InterruptedException {
    	double totalCost = 0;
    	
    	Box box = new Box();
    	box.setSize(400, 300);
    		
    	Thread.sleep(10000);
    		
    	totalCost += box.getServiceCost();
    		
		Info info = new Info();
		double zipCodeCost = info.getZipCodeCost();
		totalCost += zipCodeCost;
		
		Time time = new Time();
		System.out.println("All services you've chosen: " + 
		box.getServiceList().toString().replace("[", "").replace("]", ""));
		System.out.println("Total cost: $" + totalCost);
    }
}
