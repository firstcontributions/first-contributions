import java.lang.Math; 

public class Point {
	private double x;
	private double y;
	Point()
	{
		this.x = 0;
		this.y = 0;
	}
	Point(double a, double b)
	{
		this.x = a;
		this.y = b;
	}
	public void setX(double a)
	{
		this.x=a;
	}
	public void setY(double b) 
	{
		this.y=b;
	}
	public double getX() 
	{
		return this.x;
	}
	public double  getY() 
	{
		return this.y;
	}
	public void print() 
	{
		System.out.println("("+this.x+","+this.y+")");
	}
	public String toString() 
	{
		return "("+this.x+","+this.y+")";
	}
	public String equLine(Point p) 
	{
		double c = this.y-slope(p)*this.x;
		return "y = "+slope(p)+"x + "+c;
	}
	public boolean isOrigin() 
	{
		if(this.x==0 && this.y==0) 
		{
			return true;
		}
		else
		{
			return false;
		}
	}
	public int whichQuadrant() 
	{
		if(this.x>0 && this.y>0) {
			return 1;
		}
		else if(this.x<0 && this.y>0) {
			return 2;
		}
		else if(this.x<0 && this.y<0) {
			return 3;
		}
		else if(this.x>0 && this.y<0) {
			return 4;
		}
		else {
			return 0;
		}
	}
	public Point xProj()
	{
		Point xp;
		xp = new Point(this.x,0);
		return xp;
	}
	public Point yProj() 
	{
		Point xp;
		xp = new Point(0,this.y);
		return xp;
	}
	public Point xRefl() 
	{
		Point xp;
		xp = new Point(this.x,-this.y);
		return xp;
	}
	public Point yRefl() 
	{
		Point xp;
		xp = new Point(-this.x,this.y);
		return xp;
	}
	public Point scalarMult(double c) 
	{
		Point sp;
		sp = new Point(c*this.x,c*this.y);
		return sp;
	}
	public Point sumPoint(Point p) 
	{
		Point sp;
		sp = new Point (this.x+p.x,this.y+p.y);
		return sp;
	}
	public double slope(Point p) 
	{
		return (double)(this.y-p.y)/(this.x-p.x);
	}
	public double distanceM(Point p)
	{
		return absolute(this.x-p.x)+absolute(this.y-p.y);  
	}
	public double distanceE(Point p)
	{
		return Math.sqrt(Math.pow(this.x-p.x,2)+Math.pow(this.y-p.y,2));
	}
	private static double absolute(double n) {
		if (n<0) {
			return -1*n;
		}
		else 
			return n;
	}
	
}
