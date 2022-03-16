import java.util.Scanner;
import java.util.Arrays;

public class wk45exercise2 {
	
	public static void displaySortedNumbers(double num1, double num2, 
											double num3) 
	{
		double[] myList = {num1, num2, num3};
		Arrays.sort(myList);
		
		System.out.print("3 numbers in increasing order: ");
		for (int i = 0; i < myList.length; i ++) {
			System.out.print(myList[i] + " ");
		}
	}
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		System.out.print("Enter 3 numbers separated by a space: ");
		double number1 = input.nextDouble();
		double number2 = input.nextDouble();
		double number3 = input.nextDouble();
		
		displaySortedNumbers(number1, number2, number3);
	}

}
