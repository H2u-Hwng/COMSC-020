/*
 *
 */

import java.util.*;

public class SortArrayList {
    /** Main method */
    public static void main(String[] args) {
        // Create an Integer ArrayList
        ArrayList<Integer> intArray = new ArrayList<>();
        intArray.add(2);
        intArray.add(4);
        intArray.add(3);
        
        // Create a Double ArrayList
        ArrayList<Double> doubleArray = new ArrayList<>();
        doubleArray.add(3.4);
        doubleArray.add(1.2);
        doubleArray.add(-12.3);
        
        // Create a String ArrayList
        ArrayList<String> stringArray = new ArrayList<>();
        stringArray.add("Bob");
        stringArray.add("Alice");
        stringArray.add("Ted");
        stringArray.add("Carol");
                  
        // Sort the ArrayLists
        sort(intArray);
        
        sort(doubleArray);
        
        sort(stringArray);

        // Display the sorted ArrayLists
        System.out.print("Sorted Integer Objects: ");
        printList(intArray);

        System.out.print("Sorted Double Objects: ");
        printList(doubleArray);

        System.out.print("Sorted String Objects: ");
        printList(stringArray);
    }
    
    /** Sort all elements in the ArrayList */
    public static <E extends Comparable<E>> void sort(ArrayList<E> list) {
        E minElement;
        int minIndex;
        
        for (int i = 0; i < list.size() - 1; i++) {
            minElement = list.get(i);
            minIndex = i;
            
            for (int j = i + 1; j < list.size(); j++) {
                if (list.get(j).compareTo(minElement) < 0) {
                    currentMin = list.get(j);
                    minIndex = j;
                }
            }
            
            // Swap the element at i with the one at minIndex if necessary;
            if (minIndex != i) {
                list.set(minIndex, list.get(i));
                list.set(i, minElement);
            }
        }
    }
    
    /** Print all elements in the ArrayList */
    public static void printList(ArrayList list) {
        for (int i = 0; i < list.size(); i++) {
            System.out.print(list.get(i) + " ");
        }
        System.out.println(); // new line
    }
}
