#include <iostream>
#include <time.h>
#include <cmath>

using namespace std;

double *array_generator(int);
void array_printer(double*, int);
void min_max(double*, int);

int main()
{
	int n;
	cout << "Enter array length: "; cin >> n;
	cout << "\nGenerated array:\n";
	double *B = array_generator(n);
	array_printer(B, n); cout << endl;
	min_max(B, n);
	system("pause");
}

double* array_generator(int length)					// генерує масив заданої довжини з
													// елементами з проміжку [-10; 10]
{
	double* array = new double[length];
	srand(time(NULL));
	for (int i = 0; i < length; i++)
		array[i] = (double(rand() % 2001) - 1000) / 100.;
	return array;
}

void array_printer(double* array, int length)		// друкує масив відомої довжини
{
	for (int i = 0; i < length; i++) cout << array[i] << " ";
	cout << endl;
}

void min_max(double *array, int length)			// шукає мін та макс модулі різниці сусідніх елементів
												// виводить іх та індекси їх елементів
{
	double a_min_max[6];						// 0 - мін; 1,2 - індекси мін; 3 - макс; 4,5 - індекси макс
	double diff = a_min_max[0] = a_min_max[3] = abs(array[1] - array[0]);
	for (int i = 1; i < length; i++)
	{
		diff = abs(array[i] - array[i-1]);		// модуль різниці сусідніх елементів
		if (diff <= a_min_max[0])				// менше мін => змінюємо мін та записуємо індекси "сусідів"
		{
			a_min_max[0] = diff;
			a_min_max[1] = double(i) - 1; a_min_max[2] = i;
		}
		if (diff >= a_min_max[3])				// більше макс => змінюємо макс та записуємо індекси "сусідів"
		{
			a_min_max[3] = diff;
			a_min_max[4] = double(i) - 1; a_min_max[5] = i;
		}
	}
	cout << "Minimal modulus of adjacent numbers' subtraction is " << a_min_max[0] << endl
		 << "Its number indexes are " << a_min_max[1] << " and " << a_min_max[2] << endl << endl;
	cout << "Maximal modulus of adjacent numbers' subtraction is " << a_min_max[3] << endl
		 << "Its number indexes are " << a_min_max[4] << " and " << a_min_max[5] << endl << endl;
}