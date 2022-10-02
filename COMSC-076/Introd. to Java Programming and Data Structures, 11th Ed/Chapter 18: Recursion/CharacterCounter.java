/*
 * Huu Hung Nguyen
 * 10/01/2022
 * Test #1 - Program
 * Write a method that uses recursion to count the number of times 
 * a specific character occurs in an array of characters.
 * Demonstrate the method with a driver program called CharacterCounter,
 * that prompts the user to enter a character,
 * then displays the number of occurrences of the character in the array.
 */

import java.util.*;

public class CharacterCounter {
    /** Main method */
    public static void main(String[] args) {
        // Create a scanner
        Scanner input = new Scanner(System.in);
        
        // Prompt the user for a character
        System.out.print("Enter a character: ");
        char ch = input.next().charAt(0);
        
        // The array of characters
        char[] test = {'T', 'h', 'i', 's', ' ', 'i', 's', ' ', 't', 'h', 'e', ' ', 's', 't', 'r', 'i', 'n', 'g'};
        
        // Count the number of times the character appears and display it
        int count = charCount(test, 0, ch);
        System.out.println("The occurrence number of the character in the array is " + count);
    }
    
    /** Recursive method to count the number of times a specific character occurs in an array of characters */
    public static int charCount(char[] array, int start, char ch) {
        if (start == array.length) { // Base case
            return 0;
        } else {
            int count = (array[start] == ch) ? 1 : 0;
            
            return count + charCount(array, start + 1, ch); // Recursive call
        }
    }
}
