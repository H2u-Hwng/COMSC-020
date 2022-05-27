import java.util.Scanner;

public class Quadratic {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		System.out.print("Enter a, b, and c: ");
		double a = input.nextDouble();
		double b = input.nextDouble();
		double c = input.nextDouble();
		
		double discriminant = b*b - 4*a*c;
		if (discriminant < 0) {
			System.out.println("This equation has no real roots.");
		} else if (discriminant == 0) {
			System.out.printf("The single root is %.3f", -b/(2*a));
		} else {
			System.out.printf("The roots are %.3f and %.3f", 
					(-b + Math.sqrt(discriminant))/(2*a), (-b - Math.sqrt(discriminant))/(2*a));
		}
	} 
}
