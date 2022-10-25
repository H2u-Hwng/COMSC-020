import java.util.*;

public class FindClosestPair {
    /** Main method */
    public static void main(String[] args) {
        // Create 100 random points
        Point[] p = new Point[100];
        for (int i = 0; i < p.length; i++) {
            p[i] = new Point();
            p[i].x = Math.random() * 100;
            p[i].y = Math.random() * 100;
        }

        double[][] p1 = new double[100][2];
        for (int i = 0; i < p1.length; i++) {
            p1[i][0] = p[i].x;
            p1[i][1] = p[i].y;
        }
        
        long starting, ending;
        
        starting = System.currentTimeMillis(); // get the starting time
        
	    System.out.println("Test with 1 dimentional array: ");
        System.out.println(); // new line

	    Pair pair = Pair.getClosestPair(p);

        System.out.print("The shortest distance is " + pair.getDistance());
        System.out.print(" beween the points " + pair.getP1());
        System.out.println(" and " + pair.getP2());

			// System.out.println("Test with 2-dimentional array: ");
			
			// for (int row = 0; row < p1.length; row++) 
			// { 
			// 	   System.out.println("("+ p1[row][0] +" , "+ p1[row][1]+")"); 
			// }
			//    Pair pair1 = Pair.getClosestPair(p1);
			//    System.out.println("The closet pair:");
			//     System.out.println(pair1.getP1());
			// 	System.out.println(pair1.getP2());
			// 	System.out.println("Distance: " + format.format(pair1.getDistance()));
        
        ending = System.currentTimeMillis(); // get ending time
        
        System.out.println(); // New line

        System.out.print("Time spent on the divide-and-conquer algorithm is");
        System.out.println(" " + (ending - starting) + " milliseconds");
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
            Point[] pointsPair = new Point[points.length];
            
            for (int i = 0; i < points.length; i++) {
		        pointsPair[i] = new Point(points[i][0], points[i][1]);
	        }
            
	    return getClosestPair(pointsPair);
        }
        
        /** Return the distance of the closest pair of points */
        public static Pair getClosestPair(Point[] points) {
            // Sort by x-coordinates
            Arrays.sort(points); 
            
            // Sort by y-coordinates
	    Point[] pointsOrderedOnY = points.clone(); 
	    Arrays.sort(pointsOrderedOnY, new CompareY());
		    
	    return distance(points, 0, points.length - 1, pointsOrderedOnY);
        }
        
        /** Return the distance of the closest pair of points in pointsOrderedOnX[low, high]. 
	    This is a recursive method. pointsOrderedOnX and pointsOrderedOnY are not changed
	    in the subsequent recursive calls.*/
        public static Pair distance(Point[] pointsOrderedOnX, int low, int high, Point[] pointsOrderedOnY) {
            if(low >= high) 
		{
			return null;
		} else if (low + 1 == high) 
		{
			return new Pair(pointsOrderedOnX[low], pointsOrderedOnX[high]); // only 1 pair present
		}
		
		/*
		 * Divide S into two subsets, S1 and S2, of equal size using the midpoint in the sorted list. 
		 * Let the midpoint be in S1. Recursively find the closest pair in S1 and S2. 
		 * Let d1: leftPair.getDistance()
		 * and d2: rightPair.getDistance()
		 * denote the distance of the closest pairs in the two subsets, respectively.
		 */
		int midPoint = (low + high) / 2; // divide into 2 subset 
		
		 // return the closet pair on the left side( including midpoint) - S1
		Pair leftPair = distance(pointsOrderedOnX, low, midPoint, pointsOrderedOnY);
		// return the closet pair on the right side( not including midpoint) - S2
		Pair rightPair = distance(pointsOrderedOnX, midPoint + 1, high, pointsOrderedOnY);
		
		double d = 0;
		Pair p = null;

		if (leftPair == null && rightPair == null)  // no pairs present on both sides
		{
			d = 0;
			p = null;
		} else if (leftPair == null)  // no pairs on the left side, then the right pair is the shortest
		{
			d = rightPair.getDistance(); // get d2
			p = rightPair;
		} else if (rightPair == null) // no pairs on the right side, then the left pair is the shortest
		{
			d = leftPair.getDistance(); //get d1
			p = leftPair;
		} else 
		{
			// get the minimum distance of d1 and d2: d = min(d1,d2)
			d = Math.min(leftPair.getDistance(), rightPair.getDistance());
			// get the point that has minimum distance d
			if(leftPair.getDistance() <= rightPair.getDistance())
			{
				p =leftPair;
			}else
			{
				p=rightPair;
			}
			
		}
		/*
		 * Obtaining stripL and stripR algorithm
		 * for each point p in pointsOrderedOnY
				if (p is in S1 and mid.x – p.x <= d) 
					append p to stripL;
				else if (p is in S2 and p.x - mid.x <= d) 
					append p to stripR;
		 */
		
		//create list stripL and stripR to hold the points
		ArrayList<Point> stripL = new ArrayList<Point>();
		ArrayList<Point> stripR = new ArrayList<Point>();
		for (int i = 0; i < pointsOrderedOnY.length; i++) 
		{
			if ((pointsOrderedOnY[i].getX() <= pointsOrderedOnX[midPoint].getX())&&
					(pointsOrderedOnX[midPoint].getX() - pointsOrderedOnY[i].getX() <= d)) 
			{
				stripL.add(pointsOrderedOnY[i]);
			}else if((pointsOrderedOnY[i].getX() > pointsOrderedOnX[midPoint].getX()) &&
						(pointsOrderedOnY[i].getX() - pointsOrderedOnX[midPoint].getX() <=d ))
			{
				stripR.add(pointsOrderedOnY[i]);
			}
		}

		/*
		 * finding the closet pair algorithm
		 * d = min(d1, d2);
 		   r = 0; // r is the index of a point in stripR 
 		   for (each point p in stripL) 
 		   {
				// Skip the points in stripR below p.y - d
				while (r < stripR.length && q[r].y <= p.y - d) r++;
				let r1 = r;
				while (r1 < stripR.length && |q[r1].y – p.y| <= d) 
				{
					// Check if (p, q[r1]) is a possible closest pair
					if (distance(p, q[r1]) < d) {
					d = distance(p, q[r1]);
					(p, q[r1]) is now the current closest pair;
      			}
			r1 = r1 + 1 ;
			}
		 */
		
		int r = 0;
		for (int i = 0; i < stripL.size(); i++) 
		{
			while (r < stripR.size() && stripR.get(r).getY() <= stripL.get(i).getY() - d) 
			{
				r++;
			}
			int r1 = r;
			while (r1 < stripR.size() && Math.abs(stripR.get(r1).getY() - stripL.get(i).getY()) <=  d) 
			{
				if (distance(stripL.get(i), stripR.get(r1)) < d) {
					d = distance(stripL.get(i), stripR.get(r1));
					p.p1 = stripL.get(i);
					p.p2 = stripR.get(r1);
				}
				r1++;
			}
		}

		return p;
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
