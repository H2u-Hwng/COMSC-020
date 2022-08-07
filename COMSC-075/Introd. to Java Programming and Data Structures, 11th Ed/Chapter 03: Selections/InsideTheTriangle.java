import java.util.Scanner;

public class InsideTheTriangle {
	public static void main(String[] args) {
		final int X_TRIANGLE = 200;
		final int Y_TRIANGLE = 100;
		
		Scanner input = new Scanner(System.in);
		
		System.out.print("Enter a point's x- and y-coordinates: ");
		int x = input.nextInt();
		int y = input.nextInt();
		
		if (x > X_TRIANGLE || y > Y_TRIANGLE) {
			System.out.println("The point is not in the triangle.");
		} else {
			System.out.println("The point is in the triangle.");
		}
	}
}