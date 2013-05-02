package com.bhatt.kmeans;

public class Point {
	
	public double x;
	public double y;
	//category it belongs to 
	public int category;

	
	public Point(double xh, double yh){
		x = xh;
		y = yh;
	}
	
	@Override
	public String toString() {
		return "Point [x=" + x + ", y=" + y + "]";
	}


	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
