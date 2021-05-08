#include "Lab_6.h"


int main()
{
	Triangle *TR1 = new Triangle(Point2D(1, 1), Point2D(0, -1), Point2D(-1, 1));
	Circle *C1 = new Circle(5, Point2D(TR1->GetVertexA()));
	Shape *geometry[] = { TR1, C1 };
	Point2D point = TR1->GetVertexB();
	point = Point2D(TR1->GetVertexC());

	double a = TR1->GetSideA();
	return 0;
}