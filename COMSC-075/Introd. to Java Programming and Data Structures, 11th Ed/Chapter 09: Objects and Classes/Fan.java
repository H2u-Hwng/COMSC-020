public class Fan {
    
    final int SLOW = 1;
    final int MEDIUM = 2;
    final int FAST = 3;
    
    private int speed = SLOW;
    private boolean on = false;
    private double radius = 5.0;
    
    String color = "blue";
    
    public Fan(int speed, boolean on, double radius, String color) {
        this.speed = speed;
        this.on = on;
        this.radius = radius;
        this.color = color;
    }
    
    public Fan() {
        this(1, false, 5.0, "blue");
    }
    
    public int getSpeed() {
        return speed;
    }
    
    public boolean isOn() {
        return on;
    }
    
    public double getRadius() {
        return radius;    
    }
    
    public String getColor() {
        return color;
    }
    
    public String toString() {
        if (isOn()) {
            return String.format("A %.1f inch %s fan at a speed of %d.", radius, color, speed);
        } else {
            return String.format("A %.1f inch %s fan, fan is off.", radius, color);
        }
    }
}
