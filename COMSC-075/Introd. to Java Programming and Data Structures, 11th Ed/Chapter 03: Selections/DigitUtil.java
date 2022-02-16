public class DigitUtil {

	public static boolean isSingleDigit(int n) {
		return n > -10 && n < 10;
	}
	
	public static void main(String[] args) {
		System.out.println(isSingleDigit(2));
		
		int z = 9;
		if (isSingleDigit(z)) System.out.println("z is small");
		else System.out.println("z is big");
	}
}
