#include <iostream>
#include <cmath>
using namespace std;
int main()
{
	cout << "Denys Adamov IC-01" << endl;
	float x, y;
	cout << "Enter X coordinate: ";
	cin >> x;
	cout << "Enter Y coordinate: ";
	cin >> y;
	
	if (abs(x + y) + abs(x - y) <= 6) // чи належить точка квадрату
	{
		if (x * x + y * y >= 9) // чи не належить точка кругу
		{
			if (abs(x + y) + x - y >= 0) // чи не належить другій чверті
			{
				cout << "The point belongs to the area\n";
			}
			else cout << "The point does't belong to the area\n";
		}
		else cout << "The point does't belong to the area\n";
	}
	else cout << "The point does't belong to the area\n";
	system("pause");
	return 0;
}