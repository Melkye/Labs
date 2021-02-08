#include <iostream>
#include <cmath>
using namespace std;
int main()
{
	cout << "Denys Adamov IC-01" << endl;
	float Square1_Area, Square2_Diagonal, Square2_Area, N;
	cout << "Enter 1st square's area:" << endl;
	cin >> Square1_Area;											//введення площі першого квадрата

	Square2_Diagonal = sqrt(Square1_Area);							// знаходження діагоналі вписаного квадрата через посередництво кола
	Square2_Area = Square2_Diagonal * Square2_Diagonal / 2;			// знаходження площі вписаного квадрата
	N = Square1_Area / Square2_Area;								// у скільки раз другий менший, ніж перший

	cout << "2nd square's area: " << Square2_Area << endl			// виведення площі другого квадрата
		<< "2nd is " << N << " times smaller than 1st" << endl;		// та отриманого N
	system("pause");
	return 0;
}