
public class TestRectangle {

	public static void main(String[] args) {
		Rectangle r1 = new Rectangle();
		Rectangle r2 = new Rectangle(3.0, 5.5);
		
		double area1 = r1.getArea();
		double perimeter1 = r1.getPerimeter();
		System.out.printf("area: %f perimeter: %f\n", area1, perimeter1);
		
		System.out.printf("area: %f perimeter: %f\n", r2.getArea(), r2.getPerimeter());
	}
}
