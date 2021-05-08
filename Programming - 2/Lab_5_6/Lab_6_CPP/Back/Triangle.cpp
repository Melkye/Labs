#include <cmath>
#include "Triangle.h"

Triangle::Triangle(Point2D A, Point2D B, Point2D C)
{
    if ((A.x == B.x && B.x == C.x) || (A.y == B.y && B.y == C.y))
    {
        throw "Vertexes can't be on the same line";
    }
    _vertexA = A;
    _vertexB = B;
    _vertexC = C;
}

Point2D Triangle::GetVertexA() { return _vertexA; }
Point2D Triangle::GetVertexB() { return _vertexB; }
Point2D Triangle::GetVertexC() { return _vertexC; }

double Triangle::GetSideA() { return GetDistance(_vertexB, _vertexC); }
double Triangle::GetSideB() { return GetDistance(_vertexA, _vertexC); }
double Triangle::GetSideC() { return GetDistance(_vertexA, _vertexB); }

double Triangle::GetPerimeter() { return GetSideA() + GetSideB() + GetSideC(); }
double Triangle::GetArea()
{
    return  sqrt((GetPerimeter() / 2) * (GetPerimeter() / 2 - GetSideA()) * 
    (GetPerimeter() / 2 - GetSideB()) * (GetPerimeter() / 2 - GetSideC()));
}