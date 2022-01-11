import java.util.Scanner;

public class ReverseString {
    
    public static String reverse(String s) {
        String result = "";
        
        for (int i = s.length() - 1; i >= 0; i--) {
            result += s.charAt(i);    
        }
        
        return result;
    }
    
    public static void newLine() {
        System.out.println();
    }
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter a sentence: ");
        String sentence = in.nextLine();
        
        newLine();
        
        System.out.println(reverse(sentence));
    }
}
