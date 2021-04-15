#pragma once
#include "Point2D.h"

class Square
{
	friend Square operator+(double addedCoord, Square square);
public:
	Square();
	Square(Point2D A, Point2D B, Point2D C, Point2D D);

	enum class VertexName {A, B, C, D};

	Point2D GetVertex(enum class VertexName vertex);
	double GetSide();
	double GetPerimeter();
	double GetArea();

	Square operator+(double addedCoord);
	Square operator-(double substrCoord);
	Square operator/(Square rightSquare);

private:

	Point2D _vertexA = Point2D(1, 1);
	Point2D _vertexB = Point2D(1, -1);
	Point2D _vertexC = Point2D(-1, -1);
	Point2D _vertexD = Point2D(-1, 1);

	double static GetDistance(Point2D A, Point2D B);
	Point2D GetCenter();
};

