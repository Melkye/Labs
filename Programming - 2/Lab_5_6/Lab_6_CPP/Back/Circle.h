#pragma once
#include "Shape.h"

class Circle final : public Shape
{
public:
    Circle(double r);
    Circle(double r, Point2D c);

    double GetRadius();
    Point2D GetCenter();

    double GetPerimeter();
    double GetArea();

private:
    double _radius;
    Point2D _center = Point2D(0, 0);
};