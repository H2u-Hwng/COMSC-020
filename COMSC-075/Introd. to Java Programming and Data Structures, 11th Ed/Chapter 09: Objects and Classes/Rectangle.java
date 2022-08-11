public class Rectangle {
    
    // properties
    private double width = 1.0;
    private double height = 1.0;
    
    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }
    
    public Rectangle() {
        this(1.0, 1.0);
    }
    
    public double getWidth() {
        return width;
    }
    
    public double getHeight() {
        return height;
    }
    
    public double getArea() {
        return width * height;
    }
    
    public double getPerimeter() {
        return (width + height) * 2.0;
    }
    
    public void show() {
        System.out.printf(
            "The area of a %.1f x %.1f Rectangle is %.2f\n", width, height, getArea());
        System.out.printf(
            "The perimeter of a %.1f x %.1f Rectangle is %.2f\n", width, height, getPerimeter());
    }
}
