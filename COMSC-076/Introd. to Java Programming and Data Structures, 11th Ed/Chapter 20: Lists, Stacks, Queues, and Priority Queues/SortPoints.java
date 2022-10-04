import java.util.*;

public class SortPoints {

    public static void main(String[] args) {
    }

    static class Point implements Comparable<Point> {
    
        double x;
        double y;
      
        Point(double x, double y) {
    	this.x = x;
    	this.y = y;
        }
    
        public double getX() {
            return x;
        }		
        
    	public double getY() {
    	    return y;
    	}
      
        @Override
        public double compareTo(Point p) {
    	    if (x != p.x) {
                return x - p.x;	
    	    } else {
    	        return y - p.y;
    	    }
        }
    
        @Override
        public String toString() {
            return "(" + x + ", " + y + ")";
        }
    }
}
