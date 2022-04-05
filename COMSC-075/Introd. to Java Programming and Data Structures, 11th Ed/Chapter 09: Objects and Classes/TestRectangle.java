
public class TestRectangle {

	public static void main(String[] args) {
		Rectangle r1 = new Rectangle();
		Rectangle r2 = new Rectangle(3.0, 5.5);
		
		double area1 = r1.getArea();
		double perimeter1 = r1.getPerimeter();
		System.out.printf("area: %,.3f perimeter: %,.3f\n", area1, perimeter1);
		r2.show();
	}
}
