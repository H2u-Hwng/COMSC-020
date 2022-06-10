import java.util.Scanner;

/* 
 * Write a program that prompts the user to enter a  
 * three-digit integer and determines whether it is a palindrome number. 
 * A number is palindrome if it reads the same 
 * from right to left and from left to right.
 */

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
