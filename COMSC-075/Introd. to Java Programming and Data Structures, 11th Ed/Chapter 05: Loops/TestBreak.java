public class TestBreak {

    public static void main(String[] args) {
        int number = 0;
        double sum = 0;
      
        while (number <= 20) {
            number ++;
            sum += number;
            if (sum >= 40) break;
        }
        
        System.out.printf("The number is %02d\nThe sum is %.2f", number, sum);
    }
}
