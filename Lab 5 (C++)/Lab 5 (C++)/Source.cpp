#include <iostream>
using namespace std;
int main()
{
	int n, n_max = 1,					// число з найбільшою сумою дільників
		 sum_i, sum_max = 0;			// сума дiльникiв числа i та найбільша така сума
	cout << "Enter the number: ";
	cin >> n;

	for (int i = 1; i < n + 1; i++)		// цикл для перевірки усіх чисел
										// від 1 до n включно
	{
		sum_i = 0;					
		for (int j = 1; j < i + 1; j++)		// цикл для пошуку дільників
											// числа і від 1 до і включно
		{
			if (i % j == 0) sum_i += j;
		}
		if (sum_i > sum_max)
		{
			sum_max = sum_i;
			n_max = i;
		}
		cout << i << " " << sum_i << endl;
	}

	cout << "Number " << n_max << " has the largest sum of divisors: " << sum_max << endl;

	system("pause");
}