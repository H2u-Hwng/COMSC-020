import java.util.*;

public class FindClosestPair {
    /** Main method */
    public static void main(String[] args) {
        // Create 100 random points
        Point[] points = new Point[100];
        for (int i = 0; i < points.length; i++) {
            points[i] = new Point();
            points[i].x = Math.random() * 100;
            points[i].y = Math.random() * 100;
        }
        
        long starting, ending;
        
        starting = System.currentTimeMillis(); // get the starting time
        
        // Sort by x-coordinates
        Arrays.sort(points);
        System.out.println("Points sorted on x-coordinates");
        // for (Point p : points) {
        //     System.out.println(p.toString());
        // }
        
        System.out.println(); // New line
        
        // Sort by y-coordinates
        Arrays.sort(points, new CompareY());
        System.out.println("Points sorted on y-coordinates");
        // for (Point p : points) {
        //     System.out.println(p.toString());
        // }
        
        ending = System.currentTimeMillis(); // get ending time
        
        System.out.println("Time spent on the divide-and-conquer algorithm is "+ (ending - starting) + " milliseconds");
    }
    
    static class Pair {
        // Data fields
        Point p1;
        Point p2;
        
        public Point getP1() {
            return p1;
        }
        
        public Point getP2() {
            return p2;
        }
        
        public double getDistance() {
            return distance(p1, p2);
        }
        
        /** Compute the distance between two points p1 and p2 */
        public static double distance(Point p1, Point p2) {
            return distance(p1.x, p1.y, p2.x, p2.y);
        }
        
        /** Compute the distance between points (x1, y1) and (x2, y2) */
        public static double distance(double x1, double y1, double x2, double y2) {
            return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
        }
    }
    
    /** Compare the points on x-coordinates. 
        If same x-coordinates, compare their y-coordinates. */
    static class Point implements Comparable<Point> {
        // Data fields
        double x;
        double y;
        
        public double getX() {
            return x;
        }		
        
    	public double getY() {
    	    return y;
    	}
      
        @Override
        public int compareTo(Point p) {
    	    if (x != p.x) {
                return (x > p.x) ? 1 : -1;
    	    } else {
    	        return (y > p.y) ? 1 : (y == p.y) ? 0 : -1;
    	    }
        }
    
        @Override
        public String toString() {
            return "(" + x + ", " + y + ")";
        }
    }
    
    /** Compare two points on their y-coordinates.
        If same y-coordinates, compare their x-coordinates. */
    static class CompareY implements Comparator<Point> {
        @Override
        public int compare(Point p1, Point p2) {
            if (p1.y != p2.y) {
                return (p1.y > p2.y) ? 1 : -1;
    	    } else {
    	        return (p1.x > p2.x) ? 1 : (p1.x == p2.x) ? 0 : -1;
    	    }
        }
    }
}
