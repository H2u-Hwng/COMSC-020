public class Circle {

  public static double computeArea(double radius) {
    return Math.PI * Math.pow(radius, 2);
  }
  
  public static void main(String[] args) {
    double diameter = 10.0;
    double area = computeArea(diameter / 2);
    System.out.printf("The circle's area having diaemter %.3f is %.3f", diameter, area);
  }
}
