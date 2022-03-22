import java.util.Scanner;

public class Test {

    public static void main(String[] args) {
        final double ACRE_PER_SQUARE_FEET = 43560;
        
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter length of field in feet: ");
        double length = input.nextDouble();
        
        System.out.print("Enter width of field in feet: ");
        double width = input.nextDouble();
        
        double areaInSquareFeet = length * width;
        double areaInAcres = areaInSquareFeet / ACRE_PER_SQUARE_FEET;
        System.out.printf("%.1f square feet is %.1f acres", areaInSquareFeet, areaInAcres);
    }
}
