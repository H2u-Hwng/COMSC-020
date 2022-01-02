import java.util.Scanner;

public class CheckNumber2 {
    
    public static boolean isSingleDigit(int n) {
    return n > -10 && n < 10;
    }

    public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int z = in.nextInt();
    
    if (isSingleDigit(z)) {
        System.out.println("z is small");
    } else {
        System.out.println("z is big");
    }
    }
}
