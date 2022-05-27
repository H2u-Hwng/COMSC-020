import java.util.Scanner;

public class Palindrome {
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("Enter a three-digit integer: ");
		int num = input.nextInt();
		
		int originalNum = num;
		int reversedNum = 0;
		int remainder = 0;
		
		while (num != 0) {
			remainder = num % 10;
			reversedNum = reversedNum * 10 + remainder;
			num /= 10;
		}
		
		if (originalNum == reversedNum) {
			System.out.println(originalNum + " is palindrome.");
		} else {
			System.out.println(originalNum + " is not palindrome.");
		}
	}
}
