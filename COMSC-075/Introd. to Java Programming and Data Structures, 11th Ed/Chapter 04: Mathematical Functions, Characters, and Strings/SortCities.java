import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;

public class SortCities {
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String[] cities = new String[3];

        System.out.print("Enter the first city: ");
        cities[0] = input.nextLine();

        System.out.print("Enter the second city: ");
        cities[1] = input.nextLine();

        System.out.print("Enter the third city: ");
        cities[2] = input.nextLine();

        Arrays.sort(cities);

        System.out.print("The three cities in alphabetical order are ");
        System.out.println(Arrays.toString(cities).replace("[", "").replace("]", "."));
    }
}
