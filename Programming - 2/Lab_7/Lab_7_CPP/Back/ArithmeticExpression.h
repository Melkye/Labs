#pragma once
class ArithmeticExpression
{
private:
	int a;
	int b;
	int c;
	int d;

public:
	ArithmeticExpression();
	ArithmeticExpression(int a, int b, int c, int d);
	double Calculate();
};

