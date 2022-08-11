class Fan {
    
    final int SLOW = 1;
    final int MEDIUM = 2;
    final int FAST = 3;
    
    private int speed = SLOW;
    private boolean on = false;
    private double radius = 5;
    
    String color = "blue";
    
    public Fan(int speed, boolean on, double radius, String color) {
        this.speed = speed;
        this.on = on;
        this.radius = radius;
        this.color = color;
    }
    
    public Fan() {
        this(SLOW, false, 5, "blue")
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
    
    public void toString() {
        if (isOn) {
            System.out.print
        }
    }
}
