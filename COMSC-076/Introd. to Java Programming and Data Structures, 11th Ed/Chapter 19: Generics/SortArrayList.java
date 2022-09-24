import java.util.*;

public class SortArrayList {

    public static void main(String[] args) {

        // Create an Integer array
        Integer[] intArray = {new Integer(2), 
                              new Integer(4), 
                              new Integer(3)};
        
        // Create a Double array
        Double[] doubleArray = {new Double(3.4), 
                                new Double(1.2),
                                new Double(-12.3)};

        // Create a String array
        String[] stringArray = {"Bob", "Alice", "Ted", "Carol"};

        // Sort the arrays
        sort(intArray);

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
  /** Print an array of objects */

  public static void printList(Object[] list) {

    for (int i = 0; i < list.length; i++)

      System.out.print(list[i] + " ");

    System.out.println();

  }

}




    // /** Sort an array of comparable objects */
    // public static void sort(Comparable[] list) {

    // Comparable currentMax;

    // int currentMaxIndex;



    // for (int i = list.length - 1; i >= 1; i--) {

    //   // Find the maximum in the list[0..i]
    //   currentMax = list[i];

    //   currentMaxIndex = i;



    //   for (int j = i - 1; j >= 0; j--) {

    //     if (currentMax.compareTo(list[j]) < 0) {

    //       currentMax = list[j];

    //       currentMaxIndex = j;

    //     }

    //   }



    //   // Swap list[i] with list[currentMaxIndex] if necessary;
    //   if (currentMaxIndex != i) {

    //     list[currentMaxIndex] = list[i];

    //     list[i] = currentMax;

    //   }

    // }
