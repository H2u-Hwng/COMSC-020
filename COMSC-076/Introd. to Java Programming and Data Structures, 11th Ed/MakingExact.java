import java.util.Scanner;

public class MakingExact {
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Money = $");
        double money = input.nextDouble();
        
        double[] bills = {100, 50, 20, 10, 5, 1, 0.5, 0.25, 0.1, 0.01};
        
        for (double n: bills) {
            if (money >= n) {
                int count = (int) (money / n);
               
                if (money >= 1 && count > 1) {
                    System.out.printf("%d $%.0f bills \n", count, n);
                } else if (money >= 1) {
                    System.out.printf("%d $%.0f bill \n", count, n);
                } else if (money < 1 && count > 1) {
                   System.out.printf("%d %.0f-cent coins \n", count, n*100);
                } else {
                    System.out.printf("%d %.0f-cent coin \n", count, n*100);
                }

                money -= count * n;
                money = Double.parseDouble(String.format("%.2f", money));
            }
        }
    }
}
