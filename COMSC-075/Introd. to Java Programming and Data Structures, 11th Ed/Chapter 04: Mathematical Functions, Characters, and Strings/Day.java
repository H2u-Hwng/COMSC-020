import java.util.Scanner;

public class Day {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter a number in the range of 1 through 7: ");
        int number = input.nextInt();
        
        switch (number) {
        case 1: 
            System.out.println("Monday");
            break;
        case 2:
            System.out.println("Tuesday");
            break;
        case 3:
            System.out.println("Wednesday");
            break;
        case 4:
            System.out.println("Thursday");
            break;
        case 5:
            System.out.println("Friday");
            break;
        case 6:
            System.out.println("Saturday");
            break;
        case 7:
            System.out.println("Sunday");
            break;
        default:
            System.out.print("ERROR! ");
            System.out.println("The number is outside the range of 1 through 7.");    
        }
    }
}
