import java.util.Scanner;

public class TypeFood {
    
    public static void newLine() {
        System.out.println();
    }
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
      
        System.out.print("Enter a food: "); 
        String food = in.nextLine(); // prompt the user for a food
      
        newLine(); // for readability
      
        switch (food) {
            case "apple":
            case "banana":
            case "cherry":
                System.out.println("Its type: Fruit!");
                break;
            case "asparagus":
            case "broccoli":
            case "carrot":
                System.out.println("Its type: Vegetable!");
                break;
            default:
                System.out.println("Its type: Unknown!");
                break;
        }
    }
}
