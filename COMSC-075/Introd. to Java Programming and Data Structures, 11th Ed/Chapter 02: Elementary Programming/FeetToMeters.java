import java.util.Scanner;

public class FeetToMeters {
	
	public static void main(String[] args) {
		Scanner stdin = new Scanner(System.in);
		System.out.print("Enter a value for feet: ");
		double feet = stdin.nextDouble(); 
		
		double meters = feet * 0.305;
		System.out.println(feet + " feet is " + meters + " meters");
	}
}
