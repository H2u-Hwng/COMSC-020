class Point implements Comparable<Point> {

    public double x;
    public double y;
  
    public Point(int x, int y)
		{
			this.x=x;
			this.y=y;
		}

		public int getX() {return x;}		
		public int getY() {return y;}
  
    @Override
    public int compareTo(Point o) {

        if (x > o.x)
            return 1;
        else if (x < o.x)
            return -1;
        else if (y > o.y)
            return 1;
        else if (y < o.y)
            return -1;
        else
            return 0;
    }

    @Override
    public String toString() {
        return "(" + String.format("%.2f",x) + ", " + String.format("%.2f",y) + ")";
    }
}
