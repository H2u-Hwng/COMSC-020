public class TestMax {

	/** Return the max between two numbers */
	public static int max(int num1, int num2) {
	    int result = num1;

	    if (num1 < num2) result = num2;

	    return result;
	}
	
	/** Main method */
	public static void main(String[] args) {
		int i = 5;
		int j = 2;
		int k = max(i, j);
		
		System.out.printf("The maximum between %d and %d is %d.", i, j, k);
	}
}
