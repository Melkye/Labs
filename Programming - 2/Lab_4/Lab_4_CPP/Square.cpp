#include <cmath>
#include "Square.h"

Square operator+(double addedCoord, Square square)
{
    return Square(Point2D(addedCoord + square._vertexA.x, addedCoord + square._vertexA.y),
        Point2D(addedCoord + square._vertexB.x, addedCoord + square._vertexB.y),
        Point2D(addedCoord + square._vertexC.x, addedCoord + square._vertexC.y),
        Point2D(addedCoord + square._vertexD.x, addedCoord + square._vertexD.y));
}

Square::Square() {};

Square::Square(Point2D A, Point2D B, Point2D C, Point2D D)
{
    if (GetDistance(A, B) != GetDistance(B, C) || GetDistance(A, B) != GetDistance(C, D) ||
        GetDistance(A, B) != GetDistance(A, D) ||                                           // AB
        GetDistance(B, C) != GetDistance(C, D) || GetDistance(B, C) != GetDistance(A, D) || // BC
        GetDistance(C, D) != GetDistance(A, D))                                             // CD
        throw "Distances between vertexes are not equal";

    if ((A.x == B.x && A.y == B.y) || (A.x == C.x && A.y == C.y) || (A.x == D.x && A.y == D.y) || // A
        (B.x == C.x && B.y == C.y) || (B.x == D.x && B.y == D.y) ||                               // B
        (C.x == D.x && C.y == D.y))                                                               // C
        throw "Two vertexex can't be at the same point";

    if (GetDistance(A, C) != GetDistance(B, D))
        throw "Diagonals are not equal";

    _vertexA = Point2D(A.x, A.y);
    _vertexB = Point2D(B.x, B.y);
    _vertexC = Point2D(C.x, C.y);
    _vertexD = Point2D(D.x, D.y);
}

Point2D Square::GetVertex(enum class VertexName vertex)
{
    switch (vertex)
    {
    case Square::VertexName::A:
        return _vertexA;
    case Square::VertexName::B:
        return _vertexB;
    case Square::VertexName::C:
        return _vertexC;
    case Square::VertexName::D:
        return _vertexD;
    default:
        throw "Vertex not found";
    }
}

double Square::GetSide() { return GetDistance(_vertexA, _vertexB); }
double Square::GetPerimeter() { return 4 * GetSide(); }
double Square::GetArea() { return GetSide() * GetSide(); }

Square Square::operator+(double addedCoord)
{
    return Square(Point2D(_vertexA.x + addedCoord, _vertexA.y + addedCoord),
        Point2D(_vertexB.x + addedCoord, _vertexB.y + addedCoord),
        Point2D(_vertexC.x + addedCoord, _vertexC.y + addedCoord),
        Point2D(_vertexD.x + addedCoord, _vertexD.y + addedCoord));
}

Square Square::operator-(double substrCoord)
{
    return Square(Point2D(_vertexA.x - substrCoord, _vertexA.y - substrCoord),
        Point2D(_vertexB.x - substrCoord, _vertexB.y - substrCoord),
        Point2D(_vertexC.x - substrCoord, _vertexC.y - substrCoord),
        Point2D(_vertexD.x - substrCoord, _vertexD.y - substrCoord));
}

Square Square::operator/(Square rightSquare)
{
    double newSide = GetDistance(this->GetCenter(), rightSquare.GetCenter());
    return Square(Point2D(newSide / 2, newSide / 2), Point2D(newSide / 2, -newSide / 2),
        Point2D(-newSide / 2, -newSide / 2), Point2D(-newSide / 2, newSide / 2));
}

double Square::GetDistance(Point2D A, Point2D B)
{
    return sqrt((A.x - B.x) * (A.x - B.x) + (A.y - B.y) * (A.y - B.y));
}

Point2D Square::GetCenter()
{
    return Point2D((_vertexA.x + _vertexC.x) / 2, (_vertexA.y + _vertexC.y) / 2);
}