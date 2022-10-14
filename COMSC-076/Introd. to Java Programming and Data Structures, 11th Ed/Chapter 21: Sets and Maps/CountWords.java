import java.util.*;

public class CountWords {
    
    public static void main(String[] args) {
        Map<String, Integer> map = new HashMap<>();
        String[] list = {"hello", "hi", "bye", "hi", "hello", "hi"};
        for (String word: list) {
            System.out.println(word);
            if (map.containsKey(word)) {
                map.put(word, map.get(word) + 1);
            } else {
                map.put(word, 1);
            }
        }
        System.out.println(map);
    }
}
