import java.util.*;

public class CountOccurrenceOfWords {
    
    public static void main(String[] args) throws Exception {
        // //Check command-line argument length
        // if(args.length != 1) {
        //     System.out.println("Usage: Excersice Chapter 21textFileName");System.exit(1);}
            
        // //Check if file is exist
        // File file = new File(args[0]);if(!file.exists()) {
        
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
