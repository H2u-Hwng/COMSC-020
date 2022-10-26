public class InsertionSort {
  /** Main method */
  public static void main(String[] args) {
    int[] list = {35, 18, 44, 93, 58, 29, 96, 82, 98, 8};
    
    insertionSort(list);
    
    for (int i = 0; i < list.length; i++)
      System.out.print(list[i] + " ");
  }
  
  /** Insertion sort method */
  public static void insertionSort(int[] list) {
    for (int i = 1; i < list.length; i++) {
      /** insert list[i] into a sorted sublist list[0..i-1] so that
          list[0..i] is sorted. */
      int currentElement = list[i];
      
      int k;
      for (k = i - 1; k >= 0 && list[k] > currentElement; k--) {
        list[k + 1] = list[k];
      }

      // Insert the current element into list[k+1]
      list[k + 1] = currentElement;
    }
  }
}
