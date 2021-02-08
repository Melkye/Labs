#include <iostream>
using namespace std;

int main()
{
	void amicable_numbers(int);
	int* divisors_sum(int);
	int n;
	cout << "Enter the max number: "; cin >> n;
	cout << "Amicable numbers are:\n";
	amicable_numbers(n);
	
	system("pause");
}

int *divisors_sum(int length) // створює динамічний масив суми власних дільників 
							  // та повертає адресу масиву
							  // індекс елемента масиву - число, до якого відноситься сума
{
	int *a_divisors_sum = new int[length+1]; // масив для власних дільників
	int sum;
	for (int i = 0; i < length + 1; i++)
	{
		sum = 0;
		for (int j = 1; j < i; j++)
		{
			if (i % j == 0) sum += j; // якщо число i ділится націло на j, j - дільник, додаємо його до суми
		}
		a_divisors_sum[i] = sum;
	}
	return a_divisors_sum; // повертаємо адресу масиву
}
void amicable_numbers(int limit)
{
	int *a_divisors_sum = divisors_sum(limit);
	
	for (int i = 0; i < limit + 1; i++) // проходимо всі числа до заданого включно
	{
		for (int j = i + 1; j < 2*i && j < limit + 1; j++) // і шукаємо для них дружнє, починаючи з наступного
														   // аби зменшити час пошуку, перебираємо лише до подвоєного числа
														   // або поки не дійдемо до кінцевого числа
		{
			if (a_divisors_sum[i] == j && a_divisors_sum[j] == i) // умова, за якої числа вважаються дружніми
			{
				cout << i << ", " << j << endl;
			}
		}
	}
}