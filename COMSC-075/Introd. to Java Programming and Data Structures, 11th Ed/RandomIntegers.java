import java.util.Random;

public class RandomIntegers {

	public static void main(String[] args) {
		Random rand = new Random(1000);
		
		for (int i = 0; i < 50; i++) {
			System.out.println(rand.nextInt(100));
		}
	}
}
