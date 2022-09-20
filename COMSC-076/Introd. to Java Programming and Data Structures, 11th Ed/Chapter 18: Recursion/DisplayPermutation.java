/*
 * Huu Hung Nguyen
 * 09/16/2022
 * Assignment 3
 * The program prompts the user to enter a string of characters.
 * Write a recursive method to print all permutations of a string.
 * write a program prompting the user to enter a string of characters,
 * and displays all of its permutations.
 */

import java.util.Scanner;

public class DisplayPermutation {
    /** Main method */
    public static void main(String[] args) {
        // Create a scanner
        Scanner input = new Scanner(System.in);
        
        // Prompt the user for a string
        System.out.print("Enter your string: ");
        String s = input.nextLine();
        
        // Display the permutation
        displayPermutation(s);
    }
    
    /** Recursive method to print all permutations of a string */
    public static void displayPermutation(String s) {
        displayPermutation("", s);
    }
        
    /** Helper method to move a character from s2 to s1 
        and recursively invokes it with new s1 and s2 */
    public static void displayPermutation(String s1, String s2) {
        int len = s2.length();
        
        if (len > 0) {
            for (int i = 0; i < len; i ++) {
                displayPermutation(s1 + s2.charAt(i), s2.substring(0, i) + s2.substring(i + 1));
            }
        } else {
            System.out.println(s1);
        }
    }
}
