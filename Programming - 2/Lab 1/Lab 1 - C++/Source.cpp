#include <iostream>

using namespace std;

void DecreaseByOne(int* number);
bool Equality(int n1, int n2);

int main()
{
	int* number = new int;
	*number = -37;
	DecreaseByOne(number);
	bool areEqual = Equality(100, 100);
	system("pause");
}

void DecreaseByOne(int* number)
{
	int mask = 1;
	while (mask)
	{
		*number ^= mask;
		mask &= *number;
		mask <<= 1;
	}
}

bool Equality(int n1, int n2)
{
	if ((n1 ^ n2) == 0)
	{
		return true;
	}
	else
	{
		return false;
	}
}