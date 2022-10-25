import java.util.*;

public class FindClosestPair {
    /** Main method */
    public static void main(String[] args) {    
        // Create an array to store 100 random points    
        double[][] points = new double[100][2];
        for (int i = 0; i < points.length; i++) {
            points[i][0] = Math.random() * 100;
            points[i][1] = Math.random() * 100;
        }
        
        long starting, ending;
        
        starting = System.currentTimeMillis(); // get starting time
        
        // for (int row = 0; row < points.length; row++) { 
		// 	System.out.println("("+ points[row][0] +" , "+ points[row][1]+")"); 
		// }

	Pair pair = Pair.getClosestPair(points);

        // Display result
        System.out.println("The shortest distance is " + pair.getDistance() +
            " beween the points " + pair.getP1() + " and " + pair.getP2());
        
        ending = System.currentTimeMillis(); // get ending time
        
        System.out.println(); // new line

        System.out.println("Time spent on the divide-and-conquer algorithm " +
                           "is " + (ending - starting) + " milliseconds");
    }
    
    static class Pair {
        // Data fields
        Point p1;
        Point p2;

        public Pair(Point p1, Point p2) {
            this.p1 = p1;
            this.p2 = p2;
        }
        
        public Point getP1() {
            return p1;
        }
        
        public Point getP2() {
            return p2;
        }
        
        public double getDistance() {
            return distance(p1, p2);
        }
        
        /** Return the distance of the closest pair of points */
        public static Pair getClosestPair(double[][] points) {
            Point[] points2 = new Point[points.length];
            
            for (int i = 0; i < points.length; i++) {
		        points2[i] = new Point(points[i][0], points[i][1]);
	        }
            
	        return getClosestPair(points2);
        }
        
        /** Return the distance of the closest pair of points */
        public static Pair getClosestPair(Point[] points) {
            Arrays.sort(points); // Sort by x-coordinates
            
	        Point[] pointsOrderedOnY = points.clone(); 
	        Arrays.sort(pointsOrderedOnY, new CompareY()); // Sort by y-coordinates
		    
	        return distance(points, 0, points.length - 1, pointsOrderedOnY);
        }
        
        /** Return the distance of the closest pair of points in pointsOrderedOnX[low, high]. 
	    This is a recursive method. pointsOrderedOnX and pointsOrderedOnY are not changed
	    in the subsequent recursive calls.*/
        public static Pair distance(Point[] pointsOrderedOnX, int low, int high, Point[] pointsOrderedOnY) {
            if(low >= high) {
			    return null;
		    } else if (low + 1 == high) {
			    return new Pair(pointsOrderedOnX[low], pointsOrderedOnX[high]); // only 1 pair present
		    }
		
            int midIndex = (low + high) / 2; // divide into 2 subset 
            
            // return the closet pair on the left side( including midpoint) - S1
            Pair s1 = distance(pointsOrderedOnX, low, midIndex, pointsOrderedOnY);
            // return the closet pair on the right side( not including midpoint) - S2
            Pair s2 = distance(pointsOrderedOnX, midIndex + 1, high, pointsOrderedOnY);
        
            double d = 0;
            Pair closestPair = null;

            if (s1 == null) {
                // no pairs on the left side, then the right pair is the shortest
                d = s2.getDistance();
                closestPair = s2;
            } else if (s2 == null) {
                // no pairs on the right side, then the left pair is the shortest
                d = s1.getDistance();
                closestPair = s1;
            } else {
                double d1 = s1.getDistance();
                double d2 = s2.getDistance();

                d = Math.min(d1, d2); // get the minimum distance of d1 and d2

                // get the point that has minimum distance d
                if (d1 <= d2) {
                    closestPair = s1;
                } else {
                    closestPair = s2;
                }
            }
		
            //create list stripL and stripR to hold the points
            ArrayList<Point> stripL = new ArrayList<Point>();
            ArrayList<Point> stripR = new ArrayList<Point>();
            for (Point p: pointsOrderedOnY) {
                Point mid = pointsOrderedOnX[midIndex];

                if ((p.x <= mid.x) && (mid.x - p.x <= d)) {
                    stripL.add(p);
                } else if((p.x > mid.x) && (p.x - mid.x <= d)) {
                    stripR.add(p);  
                }
            }

            int r = 0; // r is the index of a point in stripR

            for (Point p: stripL) {
                while (r < stripR.size() && stripR.get(r).y <= p.y - d) {
                    r++;
                }

                int r1 = r;
                while (r1 < stripR.size() && Math.abs(stripR.get(r1).y - p.y) <=  d) {
                    if (distance(p, stripR.get(r1)) < d) {
                        d = distance(p, stripR.get(r1));
                        closestPair.p1 = p;
                        closestPair.p2 = stripR.get(r1);
                    }

                    r1++;
                }
            }

		    return closestPair;
        }
        
        /** Compute the distance between two points p1 and p2 */
        public static double distance(Point p1, Point p2) {
            return distance(p1.x, p1.y, p2.x, p2.y);
        }
        
        /** Compute the distance between points (x1, y1) and (x2, y2) */
        public static double distance(double x1, double y1, 
                                      double x2, double y2) {
            return Math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
        }
    }
    
    /** Compare the points on x-coordinates. 
        If same x-coordinates, compare their y-coordinates. */
    static class Point implements Comparable<Point> {
        // Data fields
        double x;
        double y;
        
        // Constructor
	    public Point(double x, double y) {
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
