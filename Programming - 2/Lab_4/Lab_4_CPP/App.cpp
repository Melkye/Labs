#include "App.h"

int main()
{
	Point2D A = Point2D(2, 2);
	Point2D B = Point2D(2, -2);
	Point2D C = Point2D(-2, -2);
	Point2D D = Point2D(-2, 2);

	Square S1 = Square();
	Square S2 = Square(A, B, C, D);
	Square S3 = Square(S2);
	Square S4 = S2 + 5;
	Square S5 = S3 - 5;
	Square S6 = 10 + S5; // = S4
	Square S7 = S4 / S1;

	Point2D F = S4.GetVertex(Square::VertexName::A);
	double area1 = S1.GetArea();
	double side5 = S5.GetSide();
	double perimeter7 = S7.GetPerimeter();
}