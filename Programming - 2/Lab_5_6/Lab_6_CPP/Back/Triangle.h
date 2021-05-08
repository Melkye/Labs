#pragma once
#include "Shape.h"

class Triangle final : public Shape
{
public:
	Triangle(Point2D A, Point2D B, Point2D C);

	Point2D GetVertexA();
	Point2D GetVertexB();
	Point2D GetVertexC();

	double GetSideA();
	double GetSideB();
	double GetSideC();

	double GetPerimeter();
	double GetArea();

private:
	Point2D _vertexA = Point2D(0, 0);
	Point2D _vertexB = Point2D(0, 0);
	Point2D _vertexC = Point2D(0, 0);
};

