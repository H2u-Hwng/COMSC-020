
public class Rectangle {
	
	private double width, height; // properties
	
	public Rectangle() {
		width = 1.0;
		height = 1.0;
	}
	
	public Rectangle(double w, double h) {
		width = w;
		height = h;
	}
	
	public double getArea() {
		return width * height;
	}
	
	public double getPerimeter() {
		return 2.0 * (width + height);
	}
	
	public void show() {
		System.out.printf("area: %,.3f perimeter: %,.3f\n", getArea(), getPerimeter());
	}
}
