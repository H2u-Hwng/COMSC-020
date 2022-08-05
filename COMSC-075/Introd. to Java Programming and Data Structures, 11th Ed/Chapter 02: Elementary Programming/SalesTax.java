import java.util.Scanner;

public class SalesTax {
    public static void main(String[] args) {
        final double TAX_RATE = 0.06; // constant
      
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter purchase amount: ");
        double purchaseAmount = input.nextDouble();
      
        double tax = purchaseAmount * TAX_RATE;
        System.out.printf("Sales tax is %,.2f \n", tax);
    }
}
