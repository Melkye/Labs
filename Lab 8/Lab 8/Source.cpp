#include <iostream>
#include <iomanip>
#include <time.h>

using namespace std;

int** matrix_generator(int);
void matrix_printer(int**, int);
int** matrix_dupl(int**, int);
void matrix_manip(int**, int**, int);
int main()
{
	int n;
	cout << "Enter matrix order: "; cin >> n;
	cout << "\nYour matrix:\n";
	int** A = matrix_generator(n);
	matrix_printer(A, n);
	cout << "\n";
	int** B = matrix_dupl(A, n);
	matrix_manip(A, B, n);
	cout << "The modified matrix:\n";
	matrix_printer(B, n);
	system("pause");
}

int** matrix_generator(int order)   // генерує квадратну матрицю заданої довжини з 
									// випадковими цілими елементами з проміжку [0; 9]
{
	srand(time(NULL));
	int** matrix = new int*[order];
	for (int i = 0; i < order; i++)
	{
		matrix[i] = new int[order];
		for (int j = 0; j < order; j++)
		{
			matrix[i][j] = rand()%10;
		}
	}
	return matrix;
}

void matrix_printer(int** matrix, int order)  // друкує квадратну матрицю відомого порядку
{
	for (int i = 0; i < order; i++)
	{
		for (int j = 0; j < order; j++)
		{
			cout << setw(2) << matrix[i][j] << " ";
		}
		cout << endl;
	}
}

int** matrix_dupl(int** matrix_old, int order)
{
	int** matrix_new = new int* [order];
	for (int i = 0; i < order; i++)
	{
		matrix_new[i] = new int[order];
		for (int j = 0; j < order; j++)		 // проходимо кожен елемент нової матриці
		{
			matrix_new[i][j] = matrix_old[i][j];	 // привласнюємо значення зі старої матриці
		}
	}
	return matrix_new;
}

void matrix_manip(int** matrix_old, int** matrix_new, int order) // будує нову матрицю за правилом
														   // новий елемент = макс з трикутника під старим елементом
{
	for (int i = 0; i < order - 1; i++) // нижній рядок не змінюється, тому можемо його не чіпати
	{
		for (int j = 0; j < order; j++)		 // проходимо кожен елемент нової матриці
		{										
			for (int k = 0; k < order - i; k++)  // далі рухаємося трикутником
			{
				for (int p = (j - k > 0) ? j - k : 0;   // 0 - щоб не вийти за межі матриці зліва
					i + k - p >= i - j && p < order;	// p < order - щоб не вийти за межі матриці справа
					p++)
				{					
					if (matrix_old[k + i][p] > matrix_new[i][j])
						matrix_new[i][j] = matrix_old[k + i][p];
				}
			}
		}
	}
}