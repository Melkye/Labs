#include "Strings.h"

int main()
{
	cout << "Enter the number of lines you'd like to enter: ";
	int n;
	cin >> n; cin.ignore(1, '\n');

	string* a_Text = TextInput(n);
	cout << "Your text is:" << endl;
	TextPrinter(a_Text, n);
	cout << endl;

	string* a_Repeat = Repeatable(a_Text, n);
	TextPrinter(a_Repeat, n);
	system("pause");
}