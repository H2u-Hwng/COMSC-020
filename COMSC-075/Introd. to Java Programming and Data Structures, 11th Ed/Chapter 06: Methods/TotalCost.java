import java.util.Scanner;

public class TotalCost {
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter the monthly cost for loan payment: ");
        double loanPayment = input.nextDouble();
        
        System.out.print("Enterthe monthly cost for insurance: ");
        double insurance = input.nextDouble();
        
        System.out.print("Enter the monthly cost for gas: ");
        double gas = input.nextDouble();
        
        System.out.print("Enter the monthly cost for oil: ");
        double oil = input.nextDouble();
        
        System.out.print("Enter the monthly cost for tires: ");
        double tires = input.nextDouble();
        
        System.out.print("Enter the monthly cost for maintenance: ");
        double maintenance = input.nextDouble();
        
        double totalMonthlyCost = loanPayment + insurance + gas + oil + tires + maintenance;
        System.out.printf("The total monthly cost of these expenses is %,.2f \n", totalMonthlyCost);
        
        double totalAnnualCost = totalMonthlyCost * 12;
        System.out.printf("The total annual cost of these expenses is %,.2f", totalAnnualCost);
    }
}
