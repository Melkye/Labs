#include "Fun.h"

int** MatrixGenerator(int n)
{
	srand(time(NULL));
	int** matrix = new int* [n];
	for (int i = 0; i < n; i++)
	{
		matrix[i] = new int [n];
		for (int j = 0; j < n; j++)
		{
			if (i == j) matrix[i][j] = 0;
			else matrix[i][j] = rand() % 3;
		}
	}
	for (int j = 0; j < n; j++)
	{
		for (int i = 0; i < j; i++)
		{
			if (matrix[i][j] == 0) matrix[j][i] = 2;
			else if (matrix[i][j] == 1) matrix[j][i] = 1;
			else matrix[j][i] = 0;
		}
	}
	return matrix;
}

void MatrixPrinter(int** matrix, int n)
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cout << matrix[i][j] << " ";
		}
		cout << endl;
	}
}

int** ZeroLost(int** matrix, int n)
{
	int n_teams_zero = n;
	int points;
	int** table = new int*[2];

	for (int i = 0; i < n; i++)
		table[i] = new int[n];

	for (int i = 0; i < n; i++)
	{
		table[0][i] = i;
		table[1][i] = 0;				//кількість очок
		for (int j = 0; j < n; j++)
		{
			table[1][i] += matrix[i][j];
			if (matrix[i][j] == 0)
			{
				n_teams_zero--;
				for (int k = i; k < n-1; k++)
				{
					table[1][i] = table[1][i + 1];
				}
			}
		}
	}
	return table;
}

void ZeroMaker(int** matrix, int n)
{
	int max = matrix[0][0];
	for (int j = 0; j < n; j++)
	{
		for (int i = 0; i < n; i++)
		{
			if (matrix[i][j] > max) max = matrix[i][j];
		}
		for (int k = 0; k < n; k++)
		{
			if (matrix[k][j] == max) matrix[k][j] = 9;
		}
	}
}