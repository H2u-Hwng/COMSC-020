
public class TestRectangle {

	public static void main(String[] args) {
		Rectangle r1 = new Rectangle();
		double area1 = r1.getArea();
		double perimeter1 = r1.getPerimeter();
		System.out.printf("area: %,.3f perimeter: %,.3f\n", area1, perimeter1);
		
		Rectangle r2 = new Rectangle(3.0, 5.5);
		r2.show();
		
		Rectangle r3 = new Rectangle(4, 40);
        	r3.show();
        
        	Rectangle r4 = new Rectangle(3.5, 35.9);
        	r4.show();
	}
}
