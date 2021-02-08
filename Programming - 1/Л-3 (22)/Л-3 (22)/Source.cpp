#include <iostream>
#include <iomanip> 
#include <math.h>
using namespace std;
int main()
{
	cout << "Denys Adamov IC-01\n";
	double e=0, t=1, accuracy;
	int n=0, N, width, p;
	cout << "Set N numbers after decimal point: ";
	cin >> N;

	accuracy = pow(10, -N); // точність до N-го знаку
	width = N+2;			// ширина всього числа (для форматованого виведення)
	p = N+1;				// виведенняя з наступним знаком для порівняння
	do
	{
		t = (!n) ? 1 : t / n;  // елемент ряду
		cout << "t" << setw(2) << left << n << " = " << left << setw(width) << fixed << setprecision(p) << t << endl;
		e += t;
		n++;
	} while (t / n >= accuracy);

	cout << "t00 = " << t / n << endl; // елемент, який менше за точність
	cout << "a   = " << accuracy << endl;	// точність
	cout << "e   = " << e << endl;
	system("pause");
}