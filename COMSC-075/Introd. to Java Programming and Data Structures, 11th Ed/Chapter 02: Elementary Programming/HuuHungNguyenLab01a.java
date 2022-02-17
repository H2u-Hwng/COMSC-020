import java.util.Scanner;

/**
 * Prompts the user for radius and length.
 * Computes and displays the area and volume.
 */

public class HuuHungNguyenLab01a {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		System.out.print("Enter a radius: ");
		double radius = input.nextDouble(); // prompt for a radius
		
		System.out.print("Enter a length: ");
		double length = input.nextDouble(); // prompt for a length
		
		// calculate and display the area
		double area = Math.PI * radius * radius;
		System.out.println("Area = " + area);
		
		// calculate and display the volume
		double volume = area * length;
		System.out.println("Volume = " + volume);
	}
}
