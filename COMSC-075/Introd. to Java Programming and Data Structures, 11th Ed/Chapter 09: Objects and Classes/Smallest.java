import java.util.Scanner;
import java.util.Arrays;

public class Smallest {
	
	public static double min(double[] array) {
		Arrays.sort(array);
		return array[0];
	}
	
	public static void main (String[] args) {
		final int NUMBER = 10;
		
		Scanner input = new Scanner(System.in);
		
		System.out.printf(
		"Enter %d numbers separated by a space: ", NUMBER);
		double[] myList = new double[NUMBER];
		for (int i = 0; i < NUMBER; i ++) {
			myList[i] = input.nextDouble();
		}
		
		System.out.printf("The minimum value is %.3f.", min(myList));
	}
}
