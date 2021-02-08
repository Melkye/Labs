#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	cout << "Denys Adamov IC-01" << endl << "Enter natural number n: ";
	int n;
	cin >> n;
	double S = 0;
	for (double k = 1; k <= n; k++)
	{
		S = S + 1.0 / (k * (2 * k + 1) * (2 * k + 1));
	}
	cout << "Sum equals " << setprecision(10) << S << endl;
	system("pause");
}