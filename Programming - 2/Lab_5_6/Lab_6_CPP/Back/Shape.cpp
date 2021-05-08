#include <cmath>
#include "Shape.h"

double Shape::GetDistance(Point2D A, Point2D B)
{
	return sqrt((A.x - B.x) * (A.x - B.x) + (A.y - B.y) * (A.y - B.y));
}
