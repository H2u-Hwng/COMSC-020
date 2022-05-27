/**
 * Stack diagram exercise.
 */

public class Exercise {
	public static int prod(int m, int n) {
		int result;
				
		if (m == n) {
		result = n;
		} else {
		int recurse = prod(m, n - 1);
		result = n * recurse;
		}
		        
		return result;
	}
		
	public static void main(String[] args) {
		System.out.println(prod(1, 4));
	}
}
