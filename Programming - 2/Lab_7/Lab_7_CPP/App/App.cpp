#include <iostream>
#include <random>
#include "App.h"
using namespace std;

int main()
{
    const int size = 100;
    ArithmeticExpression someMath[size];
    double moreMath[size];
    for (int i = 0; i < size; i++)
    {
        someMath[i] = ArithmeticExpression(rand() % (i + 1), rand() % (i + 1), rand() % (i + 1), rand() % (i + 1));
    }

    for (int i = 0; i < size; i++)
    {
        try
        {
            moreMath[i] = someMath[i].Calculate();
        }
        catch (int e)
        {
            if (e == 1)
            {
                moreMath[i] = 0;
                cout << i + 1 << ". Error. Attempt to divide by zero. a = -4c" << endl;
            }
            else if (e == 2)
            {
                moreMath[i] = 1.1;
                cout << i + 1 << ". Error. Attempt to take logarithm of a non-positive number. 2c = d" << endl;
            }
            else
            {
                throw;
            }
        }
        catch (...)
        {
            moreMath[i] = 2.2;
            cout << i + 1 << ". Error. Real trouble happened." << endl;
        }
    }
    system("pause");
	return 0;
}