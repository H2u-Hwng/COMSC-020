import java.util.Scanner;

public class Program1 {
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter your string: ");
        String value = input.nextLine();
        
        reverseDisplay(value, value.length());
    }
    
    public static void reverseDisplay(String value) {
        reverseDisplay(value, value.length());
    }
    
    public static void reverseDisplay(String value, int high) {
        String result = "";
        
        for (int i = high - 1; i > -1; i --) {
            result += String.valueOf(value.charAt(i));
        }
        
        System.out.println(result);
    }
}
