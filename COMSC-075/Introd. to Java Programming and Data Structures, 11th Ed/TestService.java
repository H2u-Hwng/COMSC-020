import java.util.*;
class Service {
	private String doing;
	private double cost;
	
	public Service(String doing, double cost) {
		this.doing = doing;
		this.cost = cost;
	}
	
	public String getDoing() {
		return doing;
	}
	
	public double getCost() {
		return cost;
	}
}

public class TestService {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		Service[] jobs = {
				new Service("mowing", 100.0),
				new Service("tree removal", 1000.0),
				new Service("planting", 300.0)
		};
		
		String[] doings = {"mowing", "tree removal", "planting"};
		
		System.out.println("Services: mowing, tree removal, and planting.");
		System.out.println("How many services you want to choose?");
		
		while (!input.hasNextInt()) {
			System.err.printf("ERROR! %s is not a number.\nEnter an integer number.\n", 
					input.nextLine());
		}
		
		int number = input.nextInt();
		new MyFrame();
	}
}
