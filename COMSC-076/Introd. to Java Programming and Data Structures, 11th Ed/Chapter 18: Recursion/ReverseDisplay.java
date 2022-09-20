/*
 * Huu Hung Nguyen
 * 09/16/2022
 * Assignment 3
 * The program promptes the user to enter a string.
 * Write a recursive method that displays a string in reverse order.
 * The program has the method call a helper method that includes the string's high index.
 */

import java.util.Scanner;

public class ReverseDisplay {
    /** Main method */
    public static void main(String[] args) {
        // Create a scanner
        Scanner input = new Scanner(System.in);
        
        // Prompt the user for a string
        System.out.print("Enter your string: ");
        String value = input.nextLine();
        
        // Display the reversed string
        reverseDisplay(value);
    }
    
    /** Recursive method to display a string in reverse order */
    public static void reverseDisplay(String value) {
        reverseDisplay(value, value.length());
    }
    
    /** Helper method to include the string's high index */
    public static void reverseDisplay(String value, int high) {
        if (high > 0) {
            System.out.print(value.charAt(high - 1));
            reverseDisplay(value.substring(0, high - 1));
        }
    }
}
