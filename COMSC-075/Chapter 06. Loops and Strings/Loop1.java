import java.util.Scanner;

public class Loop1 {
    
    public static void newLine() {
        System.out.println();
    }
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter a number: ");
        
        int number = in.nextInt();
        
        newLine(); // for readability
        
        while (number > 0) {
            System.out.println(number);
            number -= 1;
        }
        
        System.out.println("Blastoff!");    
    }
}
