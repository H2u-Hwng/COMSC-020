import java.util.*;

public class SortArrayList {

    public static void main(String[] args) {
        // Create an Integer array
        ArrayList<Integer> intArray = new ArrayList<>();
        intArray.add(2);
        intArray.add(4);
        intArray.add(3);
        
        // Create a Double array
        ArrayList<Double> doubleArray = new ArrayList<>();
        doubleArray.add(3.4);
        doubleArray.add(1.2);
        doubleArray.add(-12.3);
        
        // Create a String array
        ArrayList<String> stringArray = new ArrayList<>();
        stringArray.add("Bob");
        stringArray.add("Alice");
        stringArray.add("Ted");
        stringArray.add("Carol");
                  
        // Sort the arrays
        Collections.sort(intArray);

        sort(doubleArray);

        sort(stringArray);

        // Display the sorted arrays
        System.out.print("Sorted Integer Objects: ");
        printList(intArray);

        System.out.print("Sorted Double Objects: ");
        printList(doubleArray);

        System.out.print("Sorted String Objects: ");
        printList(stringArray);

    }

    public static <E extends Comparable<E>> void sort(ArrayList<E> list) {


        for (int i = 0; i < list.size() - 1; i++) {
            E currentMin = list.get(i);
            int min = i;
            for (int j = i + 1; j < list.size(); j++) {

                if (list.get(j).compareTo(currentMin) < 0) {
                    currentMin = list.get(j);
                    min = j;
                }
            }

            if (min != i) {
                list.set(min, list.get(i));
                list.set(i, currentMin);
            }
        }
    }
    
    /** Print an array of objects */
    public static void printList(ArrayList list) {
        for (int i = 0; i < list.size(); i++) {
            System.out.print(list.get(i) + " ");
        }
        System.out.println();
    }
}



    public static <E extends Comparable<E>> void sort(ArrayList<E> list) {
        E currentMin;
        int currentMinIndex;
        
        for (int i = 0; i < list.size() − 1; i++) {
            // Find the minimum in the list[i+1..list.length−2]
            currentMin = list[i];
            currentMinIndex = i;

            for (int j = i + 1; j < list.size(); j++) {
                if (currentMin.compareTo(list[j]) > 0) {
                    currentMin = list[j];
                    currentMinIndex = j;
                }
            }

            // Swap list[i] with list[currentMinIndex] if necessary;
            if (currentMinIndex != i) {
                list[currentMinIndex] = list[i];
                list[i] = currentMin;
            }
        }
    }
  

}




