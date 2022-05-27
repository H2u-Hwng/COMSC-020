public class TestCircle2D {
	
	public static void main(String[] args) {
		Circle2D c1 = new Circle2D(2, 2, 5.5);
		System.out.println("The area of c1 is " + c1.getArea());
		System.out.println("The perimeter of c1 is " + c1.getPerimeter());
		System.out.println("c1 contains (3, 3): " + c1.contains(3, 3));
		
		Circle2D c2 = new Circle2D(4, 5, 10.5);
		System.out.println("c1 is inside Circle(4, 5, 10.5): " + c1.contains(c2));
		
		Circle2D c3 = new Circle2D(3, 5, 2.3);
		System.out.println("c1 overlaps circle(3, 5. 2.3): " + c1.overlaps(c3));
//		System.out.printf("%s", c3.toString());
	}
}
