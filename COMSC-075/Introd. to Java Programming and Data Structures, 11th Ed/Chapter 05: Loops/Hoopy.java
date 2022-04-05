public class Hoopy {

	public static void main(String[] args) {
		boolean flag1 = isHoopy(201);
		boolean flag2 = isFrabjuous(202);
		System.out.println(flag1);
		System.out.println(flag2);
		if (flag1 && flag2) {
			System.out.println("ping!");
		}
		if (flag1 || flag2) {
			System.out.println("pong!");
		}
	}

	public static boolean isHoopy(int x) {
		boolean hoopyFlag = (x % 2 == 0);
		return hoopyFlag;
	}

	public static boolean isFrabjuous(int x) {
		boolean frabjuousFlag = (x > 0);
		return frabjuousFlag;
	}

}
