/*
 * Huu Hung Nguyen
 * 10/18/2022
 * Assignment 6
 * The program reads the text from a text file.
 * The text file is passed as a command-line argument.
 * Words are delimited by whitespace characters, punctuation marks (, ; . : ?),
 * quotation marks (' "), and parentheses.
 * Count the words in a case-sensitive fashion. The words must start with a letter.
 * Display the output of words in alphabetical order, with each word preceded by the number of times it occurs. 
 */

import java.util.*;

public class CountOccurrenceOfWords {
    
    public static void main(String[] args) throws Exception {
        //Check command-line argument length
        if(args.length != 1) {
            System.out.println("Usage: Excersice Chapter 21textFileName");
            System.exit(1);
        }
            
        //Check if file is exist
        File file = new File(args[0]);
        if(!file.exists()) {
            System.out.println("The file " + args[0] + " does not exists.");
            System.exit(1);
        }
        
        // Set text in a string
        String text = "Good morning. Have a good class. " +
                      "Have a good visit. Have fun!";
        
        // Create a TreeMap to hold words as key and count as value
        Map<String, Integer> map = new TreeMap<>();
        
        String[] words = text.split("[ \n\t\r\"\'.,;:!?(){}]+");
        
        for (String key: words) {
            key = key.toLowerCase();
            
            if (map.containsKey(key)) {
                map.put(key, map.get(key) + 1);
            } else {
                map.put(key, 1);
            }
        }
        
        // Display key and value for each entry
        System.out.print("Display words and their count ");
        System.out.println("in ascending order of the words");
        map.forEach((k, v) -> System.out.println(k + "\t" + v));
    }
}
