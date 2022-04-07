public class IfElse {

	public static void main(String[] args) {
		int x = 0;
		int n = -17;

		if (x == 0) {
			System.out.println("x is zero");
		} else {
			System.out.println("x is not zero");
			
			if (x > 0) {
				System.out.println("x is positive");
			} else {
				System.out.println("x is negative");
			}
		}
			
		if (x % 2 == 0) {
			System.out.println("x is even");
		} else {
			System.out.println("x is odd");
		}

		if (n == 0) {
			System.out.println("n is zero");
		} else {
			System.out.println("n is not zero");
			
			if (n > 0) {
				System.out.println("n is positive");
			} else {
				System.out.println("n is negative");
			}
		}
			
		if (n % 2 == 0) {
			System.out.println("n is even");
		} else {
			System.out.println("n is odd");
		}
	}

}
