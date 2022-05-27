
public class Circle2D {
	private double x, y;
	private double radius;
	
	public Circle2D(double x, double y, double radius) {
		this.x = x;
		this.y = y;
		this.radius = radius;
	}
	
	public Circle2D() {
		this(0, 0, 1);
	}
	
	public double getX() {
		return x;
	}
	
	public double getY() {
		return y;
	}
	
	public double getRadius() {
		return radius;
	}
	
	public double getArea() {
		return radius * radius * Math.PI; 
	}
	
	public double getPerimeter() {
		return 2 * radius * Math.PI;
	}
	
	public boolean contains(double x, double y) {
		double distance = getDistance(x, y, this.x, this.y);
		return distance < radius;
	}
	
	public boolean contains(Circle2D circle) {
		double distance = getDistance(this.x, this.y, circle.x, circle.y);
		return distance < (circle.radius - this.radius);
	}
	
	public boolean overlaps(Circle2D circle) {
		double distance = getDistance(circle.x, circle.y, this.x, this.y);
		return distance > (this.radius - circle.radius) && distance < (this.radius + circle.radius);  
	}
	
	public double getDistance(double x1, double y1, double x2, double y2) {
		return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
	}
}
