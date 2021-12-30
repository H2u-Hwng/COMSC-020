public class GetDistance {
    
    public static double distance(double x1, double y1, double x2, double y2) {
        double dx = x2 - x1;
        double dy = y2 - y1;
        double dsquared = dx * dx + dy * dy;
        double result = Math.sqrt(dsquared);
        return result;
    }
    
    public static void main(String[] args) {
        System.out.println("Distance = " + distance(1, 6, 5, 9));
    }
}
