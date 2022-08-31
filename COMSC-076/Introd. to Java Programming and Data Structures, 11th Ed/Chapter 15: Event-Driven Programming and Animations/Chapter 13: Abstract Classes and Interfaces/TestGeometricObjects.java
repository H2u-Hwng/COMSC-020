/*
 * Huu Hung Nguyen
 * Assignment 1
 * 
 * Design a new Triangle class extends abstract GeometricObject class.
 * Write a test program prompts the user for three sides of the triangle,
 * and check whether they define an actual triangle.
 * It also prompts a color, and a Boolean filled.
 * It create a Triangle object with 3 sides, set the color and filled.
 * It add circle and rectangle objects with specific values.
 * It display, for each of these geometric objects, the area, perimeter, 
 * color, and true or false to indicate whether it is filled or not.
 */

package chapter13;

import java.util.Scanner;

class Rectangle extends GeometricObject {
  private double width;
  private double height;

  public Rectangle() {
  }

  public Rectangle(double width, double height) {
    this.width = width;
    this.height = height;
  }

  /** Return width */
  public double getWidth() {
    return width;
  }

  /** Set a new width */
  public void setWidth(double width) {
    this.width = width;
  }

  /** Return height */
  public double getHeight() {
    return height;
  }

  /** Set a new height */
  public void setHeight(double height) {
    this.height = height;
  }

  @Override /** Return area */
  public double getArea() {
    return width * height;
  }

  @Override /** Return perimeter */
  public double getPerimeter() {
    return 2 * (width + height);
  }
}


class Circle extends GeometricObject {
  private double radius;

  public Circle() {
  }

  public Circle(double radius) {
    this.radius = radius;
  }

  /** Return radius */
  public double getRadius() {
    return radius;
  }

  /** Set a new radius */
  public void setRadius(double radius) {
    this.radius = radius;
  }

  @Override /** Return area */
  public double getArea() {
    return radius * radius * Math.PI;
  }

  /** Return diameter */
  public double getDiameter() {
    return 2 * radius;
  }

  @Override /** Return perimeter */
  public double getPerimeter() {
    return 2 * radius * Math.PI;
  }

  /* Print the circle info */
  public void printCircle() {
    System.out.println("The circle is created " + getDateCreated() +
      " and the radius is " + radius);
  }
}


class Triangle extends GeometricObject {
  private double side1, side2, side3;

  public Triangle(double side1, double side2, double side3) {
    this.side1 = side1;
    this.side2 = side2;
    this.side3 = side3;
  }

  /** Return first side */
  public double getSide1() {
    return side1;
  }

  /** Set a new first side */
  public void setSide1(double side1) {
    this.side1 = side1;
  }

  /** Return second side */
  public double getSide2() {
    return side2;
  }

  /** Set a new second side */
  public void setSide2(double side2) {
    this.side2 = side2;
  }

  /** Return third side */
  public double getSide3() {
    return side3;
  }

  /** Set a new third side */
  public void setSide3(double side3) {
    this.side3 = side3;
  }

  @Override /** Return perimeter */
  public double getPerimeter() {
    return side1 + side2 + side3;
  }

  @Override /** Return area */
  public double getArea() {
    double semiPerimeter = getPerimeter() / 2;
    return Math.sqrt(semiPerimeter * (semiPerimeter - side1) * 
      (semiPerimeter - side2) * (semiPerimeter - side3));
  }
}


public class TestGeometricObject {
  /** Main method */
  public static void main(String[] args) {
    // Create a Scanner
    Scanner input = new Scanner(System.in);

    // Prompt the user for 3 sides of the triangle
    System.out.print("Please enter the sides of a triangle: ");
    double side1 = input.nextDouble();
    double side2 = input.nextDouble();
    double side3 = input.nextDouble();

    // Check whether 3 sides define an actual triangle
    if (side3 > (side1 + side2) || side3 < Math.abs(side1 - side2)) {
      System.out.println("Unable to create a triangle with those sides.");
    } else {
      // Declare and initialize the geometric object triangle
      GeometricObject geoObject1 = new Triangle(side1, side2, side3);

      // Prompt the user for the color and set it
      System.out.print("What is the color of the triangle: ");
      String color = input.next();
      geoObject1.setColor(color);

      // Prompt the user for being filled and set it
      System.out.print("Is the triangle filled(true/false)?: ");
      boolean filled = input.nextBoolean();
      geoObject1.setFilled(filled);

      System.out.println(); // new line

      // Display triangle
      System.out.println("Triangle:");
      displayGeometricObject(geoObject1);

      // Declare and initialize the geometric object circle
      GeometricObject geoObject2 = new Circle(2);
      geoObject2.setColor("yellow");
      geoObject2.setFilled(true);

      // Display circle
      System.out.println("Circle:");
      displayGeometricObject(geoObject2);

      // Declare and initialize the geometric object rectangle
      GeometricObject geoObject3 = new Rectangle(2, 4);
      geoObject3.setColor("red");
      geoObject3.setFilled(false);

      // Display rectangle
      System.out.println("Rectangle:");
      displayGeometricObject(geoObject3);
    }
  }

  /** A method for displaying a geometric object */
  public static void displayGeometricObject(GeometricObject object) {
    System.out.println("Area: " + Math.floor(object.getArea() * 100) / 100);
    System.out.println("Perimeter: " + Math.floor(object.getPerimeter() * 100) / 100);
    System.out.println("Color: " + object.getColor());
    System.out.println("Filled: " + object.isFilled());
    System.out.println();
  }
}