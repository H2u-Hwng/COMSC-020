import java.util.Scanner;

public class Echo {
    
    public static void main(String[] args) {
        String line;

        // create a new scanner with the specified String Object
        Scanner input = new Scanner(System.in);

        // print the next line
        System.out.print("Type something: ");
        line = input.nextLine();
        System.out.println("You said: " + line);

        // print the next line again
        System.out.print("Type something else: ");
        line = input.nextLine();
        System.out.println("You also said: " + line);
    }
}
