import java.util.Scanner;

public class CheckNumber {
    
    public static void newLine() {
        System.out.println();
    }
    
    public static int getNumber() {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        return n;
    }
    
    public static void main(String[] args) {
        int number = getNumber(); // determine an integer number
        
        if (number != 0) {
            System.out.printf("%d is not zero.", number);
            newLine(); // for readability
            if (number > 0) {
                System.out.printf("%d is positive.", number);
            } else {
                System.out.printf("%d is negative.", number);
            }
            newLine(); // for readability
            if (number % 2 == 0) {
                System.out.printf("%d is even.", number);
            } else {
                System.out.printf("%d is odd.", number);
            }
        } else {
            System.out.printf("%d is zero.", number);
        }
    }
}
