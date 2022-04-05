public class TestCircle {
	
	/** Main method */
	public static void main(String[] args) {
	    // Create a circle with radius 1
	    Circle circle1 = new Circle();
	    circle1.printArea();
	
	    // Create a circle with radius 25
	    Circle circle2 = new Circle(25);
	    circle2.printArea();
	
	    // Create a circle with radius 125
	    Circle circle3 = new Circle(125);
	    circle3.printArea();
	
	    // Modify circle radius
	    circle2.setRadius(100);
	    circle2.printArea();
	    circle2.printCircle();
	}
}
