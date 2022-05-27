import java.util.Scanner;
import java.util.Arrays;

public class Smallest {
	
	public static double min(double[] data) {
		Arrays.sort(data);
		return data[0];
	}
	
	public static void main(String[] args) {
		final int NUMBERS = 10;
		
		Scanner input = new Scanner(System.in);
		
		double[] myList = new double[NUMBERS];
		
		System.out.printf("Enter the %d elements: ", NUMBERS);
		for (int i = 0; i < NUMBERS; i ++) {
			myList[i] = input.nextDouble();
		}
		
		System.out.printf("The minimum value is %.3f\n", min(myList));
	}
}
