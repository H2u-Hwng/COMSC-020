import java.util.Scanner;

public class PrimeNumber {
    
    public static boolean isPrime(int number) {
        boolean result = true;
        
        if (number >= 2) {
            for (int divisor = 2; divisor <= number / 2; divisor ++) {
                if (number % divisor == 0) result = false;
            }
        } else {
            result = false;
        }
        
        return result;
    }
  
    public static void main(String[] args) {
        final int NUMBER_OF_PRIMES = 50;
        final int NUMBER_OF_PRIMES_PER_LINE = 10;
        
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter a number: ");
        int number = input.nextInt();
        
        System.out.println("The first 50 prime numbers are:");
      
        int count = 0;
        while (count < NUMBER_OF_PRIMES) {
            if (isPrime(number)) {
            	  count ++;
                if (count % NUMBER_OF_PRIMES_PER_LINE == 0) System.out.println(number);
                else System.out.print(number + " ");   
            }
            number ++;
        }
         
    }
}
