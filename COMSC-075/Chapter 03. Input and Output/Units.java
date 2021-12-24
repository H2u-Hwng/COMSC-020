import java.util.Scanner;

public class Units {
    
    public static void main(String[] args) {
        final double CM_PER_INCH = 2.54; // constant
        
        Scanner in = new Scanner(System.in);
        System.out.print("How many inches? "); // prompt the user for inch
        int inch = in.nextInt();

        System.out.println(); // for readability
        
        double cm = inch * CM_PER_INCH; // calculate the cm
        
        System.out.print(inch + " in = "); // display the result
        System.out.println(cm + " cm");
    }
}
