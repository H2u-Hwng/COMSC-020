import java.util.Scanner;
import java.util.Arrays;

public class Deviations {
	
	public static double[] calcDeviations(double[] data) {
		double mean = getMean(data);
		
		int len = data.length;
		double[] result = new double[len];
		for (int i = 0; i < len; i++) {
			result[i] = data[i] - mean;
		}
		
		return result;
	}
	
	public static double getMean(double[] data) {
		double sum = 0;
		for (double element: data) {
			sum += element;
		}
		
		double mean = sum / data.length;
		
		return mean;
	}
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		int nums = 0;
		boolean valid = false;
		while (!valid) {
			System.out.print("Enter number of elements: ");
			nums = input.nextInt();
			if (nums > 0) {
				valid = true;
			} else {
				System.out.println("You must enter a positive number.");
			}
		}
		
		double[] myList = new double[nums];
		System.out.printf("Please enter the %d element(s): ", nums);
		for (int i = 0; i < nums; i++) {
			myList[i] = input.nextDouble();
		}

		double mean = getMean(myList);
		System.out.printf("The average is %.1f\n", mean);
		
		double[] newData = calcDeviations(myList);
		
		System.out.println("Here is how far each item is from the average:");
		System.out.println(Arrays.toString(newData));
		
		System.out.println("-----------------------------------------------");
		
		System.out.println("Here is how far each item is from the average:");
		for (int i = 0; i < newData.length; i++) {
			System.out.printf("%.1f is %.1f ", myList[i], Math.abs(newData[i]));
			if (myList[i] < mean) {
				System.out.println("below average");
			} else {
				System.out.println("above average");
			}
		}	
	}
}
