
public class Rectangle {
	
	double width, height; // properties
	
	Rectangle() {
		width = 1.0;
		height = 1.0;
	}
	
	Rectangle(double w, double h) {
		width = w;
		height = h;
	}
	
	double getArea() {
		return width * height;
	}
	
	double getPerimeter() {
		return 2.0 * (width + height);
	}
}
