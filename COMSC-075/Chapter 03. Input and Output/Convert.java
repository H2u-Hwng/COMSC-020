/* 
 * convert centimeters to feet and inches.
 */

import java.util.Scanner;

public class Convert {
    
    public static void main(String[] args) {
        // constants
        final double CM_PER_INCH = 2.54; 
        final int IN_PER_FOOT = 12;
        
        Scanner in = new Scanner(System.in);
        
        // prompt the user and get the value
        System.out.print("Exactly how many cm? "); 
        double cm = in.nextDouble();

        System.out.println(); // for readability
        
        // convert and output the result
        int inches = (int) (cm / CM_PER_INCH);
        int feet = inches / IN_PER_FOOT; 
        int remainder = inches % IN_PER_FOOT;
        System.out.printf("%.2f cm = %d ft, %d in \n", cm, feet, remainder);
    }
}
