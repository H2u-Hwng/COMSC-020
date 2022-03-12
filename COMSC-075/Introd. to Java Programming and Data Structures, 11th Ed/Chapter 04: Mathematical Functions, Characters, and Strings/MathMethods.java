public class MathMethods {

    public static void main(String[] args) {
        double root = Math.sqrt(17.0);
        double angle = 1.5;
        double height = Math.sin(angle);
        
        // convert degrees to radians
        double degrees = 270;
        double radians1 = degrees / 180.0 * Math.PI;
        double radians2 = Math.toRadians(degrees);
        System.out.printf("%.1f degrees = %.1f radians\n", degrees, radians2);
        
        // convert radians to degrees
        double radians = 1.5;
        double degrees1 = Math.toDegrees(Math.PI);
        double degrees2 = radians * 180 / Math.PI;
        System.out.printf("%.1f radians = %.1f degrees", radians, degrees2);
        
        long x = Math.round(Math.PI * 20.0);

        // examples of composition

        double x2 = Math.cos(angle + Math.PI / 2.0);
        double x3 = Math.exp(Math.log(10.0));
        double x4 = Math.pow(2.0, 10.0);
    }

}
