public class FindExecutionTimes {
    public static void main(String[] args) {
        long startTime, endTime;
        
        startTime = System.currentTimeMillis(); 
        
        double[] list = {-2, 4.5, 5, 1, 2, -3.3};
        selectionSort(list);
        for (int i = 0; i < list.length; i++)
            System.out.print(list[i] + " ");
            
        endTime = System.currentTimeMillis(); 

        System.out.println();
        System.out.println(endTime - startTime);
        
        startTime = System.currentTimeMillis(); 
        
        double[] list2 = {-2, 4.5, 5, 1, 2, -3.3};
        quickSort(list2);
        for (int i = 0; i < list.length; i++)
            System.out.print(list[i] + " ");
        
        endTime = System.currentTimeMillis(); 
        System.out.println();
        System.out.println(endTime - startTime);
    }
    
    /** The method for sorting the numbers */
    public static void selectionSort(double[] list) {
        for (int i = 0; i < list.length - 1; i++) {
            // Find the minimum in the list[i..list.length-1]
            double currentMin = list[i];
            int currentMinIndex = i;
    
            for (int j = i + 1; j < list.length; j++) {
                if (currentMin > list[j]) {
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
    
    public static void quickSort(double[] list) {
        quickSort(list, 0, list.length - 1);
    }

    private static void quickSort(double[] list, int first, int last) {
        if (last > first) {
            int pivotIndex = partition(list, first, last);
            quickSort(list, first, pivotIndex - 1);
            quickSort(list, pivotIndex + 1, last);
        }
    }

    /** Partition the array list[first..last] */
    private static int partition(double[] list, int first, int last) {
        double pivot = list[first]; // Choose the first element as the pivot
        int low = first + 1; // Index for forward search
        int high = last; // Index for backward search
    
        while (high > low) {
            // Search forward from left
            while (low <= high && list[low] <= pivot)
                low++;

            // Search backward from right
            while (low <= high && list[high] > pivot)
                high--;

            // Swap two elements in the list
            if (high > low) {
                double temp = list[high];
                list[high] = list[low];
                list[low] = temp;
            }
        }

        while (high > first && list[high] >= pivot)
            high--;

        // Swap pivot with list[high]
        if (pivot > list[high]) {
            list[first] = list[high];
            list[high] = pivot;
            return high;
        } else {
            return first;
        }
    }
}
