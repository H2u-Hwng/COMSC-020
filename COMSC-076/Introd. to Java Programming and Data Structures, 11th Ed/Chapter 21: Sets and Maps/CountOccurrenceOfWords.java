/*
 * Huu Hung Nguyen
 * 10/18/2022
 * Assignment 6
 * The program reads the text from a text file.
 * The text file is passed as a command-line argument.
 * Words are delimited by whitespace characters, punctuation marks (,;.:?),
 * quotation marks (' "), and parentheses. Count the words in a case-sensitive
 * fashion. The words must start with a letter.
 * Display the output of words in alphabetical order, with each word preceded
 * by the number of times it occurs. 
 */

import java.util.*;
import java.io.*;

public class CountOccurrenceOfWords {
    /** Main method */
    public static void main(String[] args) {
        // Create a scanner
        Scanner input = new Scanner(System.in);

        // Prompt the user for the file path
        System.out.print("Enter the file path: ");
        File file = new File(input.next());

        try {
            // Creating an object of BufferedReader class
            BufferedReader bReader = new BufferedReader(new FileReader(file));

            // Create a TreeMap to hold words as key and count as value
            Map<String, Integer> map = new TreeMap<>();

            String line; // Declaring a string variable

            while ((line = bReader.readLine()) != null) {
                String[] words = line.split("[0-9]+|\\W+");

                for (String key: words) {
                    key = key.toLowerCase();

                    if (key.length() > 0) {
                        if (!map.containsKey(key)) {
                            map.put(key, 1);
                        } else {
                            int value = map.get(key);
                            value++;
                            map.put(key, value);
                        }
                    }
                }
            }

            // Display key and value for each entry
            System.out.print("Display words and their count ");
            System.out.println("in ascending order of the words");
            map.forEach((k, v) -> System.out.println(v + "\t" + k));
        } catch (IOException ex) {
            System.err.println("Error in opening the file!");
        }
    }
}