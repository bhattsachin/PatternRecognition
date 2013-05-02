package com.bhatt.kmeans;

import java.util.ArrayList;
import java.util.List;

public class Kmean {
	static List<Point> points = new ArrayList<Point>();
	static int rangeX = 30; // our X and Y limits
	static int rangeY = 30;
	static int kpoints = 3; // number of clusters
	static long maxIterations = 9999;
	static List<Point> kmeans = new ArrayList<Point>();
	static double maxValueEver = 99999.9;

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		generatePoints();
		plotRandomKMeans(); // random points init
		visualize();
		
		kmean();
		System.out.println("\n-------------- AFTER RUNNING KMEANS ---------------");
		
		visualize();
		for (Point pt : kmeans){
			System.out.println(pt);
		}
		

	}

	public static void kmean() {
		double dist;
		int loopcount = 0;
		int kcenter = 0;
		double sumx;
		double sumy;
		Point dummy;
		System.out.println("RUNNING K MEANS+");

		for (int i = 0; i < maxIterations; i++) {
			// find best center for each point
			dist = maxValueEver; // we will find the min distance for one of the
									// center
			kcenter = 0;
			loopcount = 0;
			for (Point pt : points) {
				for (Point meanPt : kmeans) {
					if (dist > distance(pt, meanPt)) {
						dist = distance(pt, meanPt); // method is getting called
														// twice, optimize
						kcenter = loopcount;
					}
					loopcount++;
				}
				pt.category = kcenter; // assign the center
			}

			// take average of the points and update kmean centers
			for (int m = 0; m < kpoints; m++) {// run for each center
				sumx = kmeans.get(m).x;
				sumy = kmeans.get(m).y;
				loopcount = 1;
				for (Point pt : points) {
					if (pt.category == m) {
						sumx += pt.x;
						sumy += pt.y;
						loopcount++;
					}

				}

				// now take average
				dummy = new Point(sumx / loopcount, sumy / loopcount);
				//System.out.println("i is: " + i);
				kmeans.set(m, dummy);
			}
			
			System.out.print(".");

		}
	}

	public static double distance(Point a, Point b) {
		double alpha1;
		double alpha2;
		double result;
		alpha1 = Math.pow(a.x - b.x, 2);
		alpha2 = Math.pow(a.y - b.y, 2);

		result = Math.sqrt(alpha1 * alpha2);
		return result;
	}

	public static void generatePoints() {

		// lets enumerate 100 random points over a space [0,0] to [30, 30]
		Point point;
		for (int i = 0; i < 100; i++) {
			point = new Point(Math.random() * rangeX, Math.random() * rangeY);
			points.add(point);
		}
	}

	public static void visualize() {

		boolean found = false;
		boolean centerFound = false;
		for (int y = 0; y < rangeY; y++) { // draw column
			for (int x = 0; x < rangeX; x++) { // draw each row
				found = false;
				centerFound = false;
				// first lets see if we have center point at this coordinate
				for (Point point : kmeans) {
					if (Math.abs(point.x - x) < .5 && Math.abs(point.y - y) < .5) {
						centerFound = true;
					}
				}

				for (Point point : points) {
					if (Math.abs(point.x - x) < .5 && Math.abs(point.y - y) < .5) {
						found = true;
					}
				}

				if (centerFound) {
					System.out.print("X");
				} else {

					if (found) {
						System.out.print("o");
					} else {
						System.out.print("-");// printing empty line
					}
				}

			}
			System.out.print("\n");
		}

	}

	public static void plotRandomKMeans() {
		Point pt;
		for (int k = 0; k < kpoints; k++) {
			pt = new Point(Math.random() * rangeX, Math.random() * rangeY);
			kmeans.add(pt);
		}
	}

}
