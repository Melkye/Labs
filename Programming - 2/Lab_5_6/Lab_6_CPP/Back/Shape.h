#pragma once
#include "/Repos/Labs/Programming - 2/Lab_4/Lab_4_CPP/Point2D.h"

class Shape
{
public:
	virtual double GetPerimeter() = 0;
	virtual double GetArea() = 0;

protected:
	static double GetDistance(Point2D A, Point2D B);
};

