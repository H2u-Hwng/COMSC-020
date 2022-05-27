import java.util.*;

/**
 * Palindrome exercise.
 */
public class Recurse {

    /**
     * Returns the first character of the given String.
     */
    public static char first(String s) {
        return s.charAt(0);
    }

    /**
     * Returns all but the first letter of the given String.
     */
    public static String rest(String s) {
        return s.substring(1);
    }

    /**
     * Returns all but the first and last letter of the String.
     */
    public static String middle(String s) {
        return s.substring(1, s.length() - 1);
    }

    /**
     * Returns the length of the given String.
     */
    public static int length(String s) {
        return s.length();
    }
    
    public static String reversed(String s) {
    	String reversedString = "";
    	
    	for (int i = length(s) - 1; i > -1; i --) {
    		reversedString += s.charAt(i);
    	}
    	
    	return reversedString;
    }
    
    public static void main(String[] args) {
    	Scanner input = new Scanner(System.in);
    	String sentence = input.nextLine();
    	
    	if (sentence == reversed(sentence)) System.out.println(true);
    	else System.out.println(false);
    }
}
