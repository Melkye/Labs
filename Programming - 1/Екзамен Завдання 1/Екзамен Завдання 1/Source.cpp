#include "Fun.h"

int main()
{
	cout << "Enter the number of teams: ";
	int k;
	cin >> k;
	int** m_Matches = MatrixGenerator(k);
	MatrixPrinter(m_Matches, k);

//	cout << endl;
	//ZeroMaker(m_Matches, k);
	//MatrixPrinter(m_Matches, k);

	int** m_Zero_Teams = ZeroLost(m_Matches, k);
	MatrixPrinter(m_Zero_Teams, k);
	system("pause");
}