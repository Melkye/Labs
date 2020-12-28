#include <iostream>
#include <fstream>
#include <string>

using namespace std;
int** EdgeLister(string);
int** EdgesToAdjacency(int**, int, int);
void MatrixPrinter(int**, int, int);
void BFS(int**, int);
int main()
{
	int vertexes, edges;
	ifstream input("input.txt");
	input >> vertexes >> edges;
	int** edge_list = new int* [edges];
	input.close();
	int** graph_edges = EdgeLister("input.txt");
	int** adjacency_matrix = EdgesToAdjacency(graph_edges, vertexes, edges);
	// delete edge_list??
	MatrixPrinter(adjacency_matrix, vertexes, vertexes);
	system("pause");
}
int** EdgeLister(string name_of_file)
{
	int vertexes, edges;
	ifstream input(name_of_file);
	input >> vertexes >> edges;
	int** edge_list = new int* [edges];
	for (int i = 0; i < edges; i++)
	{
		edge_list[i] = new int[2];
		input >> edge_list[i][0] >> edge_list[i][1];
	}
	input.close();
	return edge_list;
}
int** EdgesToAdjacency(int** edge_list, int vertexes, int edges)
{
	int** adjacency_matrix = new int* [vertexes];
	for (int i = 0; i < vertexes; i++)
	{
		adjacency_matrix[i] = new int[vertexes];
		for (int j = 0; j < vertexes; j++)
		{
			adjacency_matrix[i][j] = 0;
		}
	}
	for (int i = 0; i < edges; i++)
	{
		adjacency_matrix[edge_list[i][0] - 1][edge_list[i][1] - 1] = 1;
		adjacency_matrix[edge_list[i][1] - 1][edge_list[i][0] - 1] = 1;
	}
	return adjacency_matrix;
}
void MatrixPrinter(int** matrix, int rows, int columns)
{
	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < columns; j++)
		{
			cout << matrix[i][j] << " ";
		}
		cout << "\n";
	}
}
void BFS(int** edge_list, int order, int v_start)
{
	int* BFS_numbers = new int[order];
	for (int i = 0; i < order; i++) BFS_numbers[i] = 0;
	int BFS_n = 1;
	BFS_numbers[v_start - 1] = BFS_n;
	int vertex = v_start;
	string queue = to_string(v_start) + '.';
	/*for (int i = 0; queue; i++, BFS_n++) // /////проходить треугольнику над главной диагональю
	{
		
		if (edge_list[vertex-1][i] == 1)
		{
			BFS_numbers[vertex - 1] = BFS_n; // вернуться к булевому массиву и просто выводить нынешний BFS-номер?
		}
		cout
		
	}*/
}