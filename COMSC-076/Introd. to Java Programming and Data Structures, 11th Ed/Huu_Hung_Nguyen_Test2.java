/*
 * Huu Hung Nguyen
 * 11/05/2022
 * Test #2 - Program
 * Write the following two generic methods using merge sort. The first
 * sorts the elements using the Comparable interface, and the second uses
 * the Comparator interface.
 */

import java.util.*;

public class Huu_Hung_Nguyen_Test2 {
    /** Main method */
    public static void main(String[] args) {
        Integer[] list = {2, 3, 2, 5, 6, 1, -2, 3, 14, 12};
        mergeSort(list);
        for (int i = 0; i < list.length; i++) {
            System.out.print(list[i] + " ");
        }

        System.out.println(); // new line
  
        Circle[] list1 = {new Circle(2), new Circle(3), new Circle(2), 
                          new Circle(5), new Circle(6), new Circle(1), 
                          new Circle(2), new Circle(3), new Circle(14), 
                          new Circle(12)};
        mergeSort(list1, new CircleComparator());
        for (int i = 0; i < list1.length; i++) {
            System.out.print(list1[i].getRadius() + " ");
        }
    }

    /** The sorting method using the Comparable interface */
    public static <E extends Comparable<E>> void mergeSort(E[] list) {
        if (list.length > 1) {
            // Merge sort the first half
            E[] firstHalf = (E[]) new Comparable[list.length / 2];
            System.arraycopy(list, 0, firstHalf, 0, list.length / 2);
            mergeSort(firstHalf);
         
            // Merge sort the second half
            int secondHalfLength = list.length - list.length / 2;
            E[] secondHalf = (E[]) new Comparable[secondHalfLength];
            System.arraycopy(list, list.length / 2, secondHalf, 0,
                             secondHalfLength);
            mergeSort(secondHalf);
         
            // Merge firstHalf with secondHalf into list
            int current1 = 0; // Current index in list1
            int current2 = 0; // Current index in list2
            int current3 = 0; // Current index in temp

            while (current1 < firstHalf.length && 
                   current2 < secondHalf.length) {
                if (firstHalf[current1].compareTo(secondHalf[current2]) < 0) {
                    list[current3++] = firstHalf[current1++];
                } else {
                    list[current3++] = secondHalf[current2++];
                }
            }

            // Collect remaining elements 
            while (current1 < firstHalf.length) {
                list[current3++] = firstHalf[current1++];
            }
          
            while (current2 < secondHalf.length) {
                list[current3++] = secondHalf[current2++];
            }
        }
    }

    /** The sorting method using the Comparator interface */
    public static <E> void mergeSort(E[] list, 
                                     Comparator<? super E> comparator) {
        if (list.length > 1) {
            // Merge sort the first half
            E[] firstHalf = (E[]) new Object[list.length / 2]; 
            for(int i = 0; i < list.length / 2; i++) {                
                firstHalf[i] = list[i];            
            }
            mergeSort(firstHalf, comparator);   

            // Merge sort the second half   
            int secondHalfLength = list.length - list.length / 2;
            E[] secondHalf = (E[]) new Object[secondHalfLength];            
            for(int i = list.length / 2; i < list.length; i++) {                
                secondHalf[i - list.length / 2] = list[i];
            }            
            mergeSort(secondHalf, comparator); 
            
            // Merge firstHalf with secondHalf into list
            int current1 = 0; // Current index in list1
            int current2 = 0; // Current index in list2
            int current3 = 0; // Current index in temp
    
            while (current1 < firstHalf.length && 
                   current2 < secondHalf.length) {
                if (comparator.compare(firstHalf[current1],
                                       secondHalf[current2]) < 0) {
                    list[current3++] = firstHalf[current1++];
                } else {
                    list[current3++] = secondHalf[current2++];
                }
            }

            // Collect remaining elements 
            while (current1 < firstHalf.length) {
                list[current3++] = firstHalf[current1++];
            }
    
            while (current2 < secondHalf.length) {
                list[current3++] = secondHalf[current2++];
            }
        }
    }
}
 
class CircleComparator implements Comparator<Circle> {
    public int compare(Circle c1, Circle c2) {
        int radius1 = c1.getRadius();
        int radius2 = c2.getRadius();

        return (radius1 > radius2) ? 1 : (radius1 == radius2) ? 0 : -1;
    }
}

class Circle {
    private int radius;
    
    public Circle() {
    }

    public Circle(int radius) {
        this.radius = radius;
    }
  
    /** Return radius */
    public int getRadius() {
        return radius;
    }
  
    /** Set a new radius */
    public void setRadius(int radius) {
        this.radius = radius;
    }
}