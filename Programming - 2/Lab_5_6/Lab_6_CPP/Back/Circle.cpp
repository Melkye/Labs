#include "Circle.h"

Circle::Circle(double r)
{
    if (r <= 0)
        throw "Radius must be positive";

    _radius = r;
}

Circle::Circle(double r, Point2D c) : Circle::Circle(r)
{
    _center = c;
}

double Circle::GetRadius() { return _radius; }
Point2D Circle::GetCenter() { return _center; }

double Circle::GetPerimeter() { return 2 * 3.14 * _radius; }
double Circle::GetArea() { return 3.14 * _radius * _radius; }