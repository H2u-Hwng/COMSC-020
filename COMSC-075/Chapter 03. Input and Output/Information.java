import java.util.Scanner;

public class Information {
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        // prompt the user and get the values
        System.out.print("What is your name? ");
        String name = in.nextLine();
        
        System.out.println(); // for readability
        
        System.out.print("What is your age? ");
        int age = in.nextInt();
        
        System.out.println(); // for readability
        
        // display the result
        System.out.printf("Hello %s, age %d. \n", name, age);
    }
}
