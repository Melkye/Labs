#include <iostream>
#include "Strings.h"

int main()
{
	cout << "Enter the numbers: \n";
	string s;
	getline(cin, s);
	cout << "The sum is " << Sum(s) << endl;
	system("pause");
}