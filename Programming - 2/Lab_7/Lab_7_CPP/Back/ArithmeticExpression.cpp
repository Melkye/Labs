#include "ArithmeticExpression.h"
#include <cmath>

ArithmeticExpression::ArithmeticExpression() : ArithmeticExpression(0, 0, 0, 0)
{ }

ArithmeticExpression::ArithmeticExpression(int a, int b, int c, int d)
{
	this->a = a;
	this->b = b;
	this->c = c;
	this->d = d;
}

double ArithmeticExpression::Calculate()
{
    double denom = a / 4 + c;
    double antilog = 2 * c - d;
    if (denom == 0)
        throw 1;
    if (antilog <= 0)
        throw 2;
    return (log10(antilog) + d - 152) / denom;
}
