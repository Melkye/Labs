#include "Lab_8.h"

int main()
{
	LinkedList list(1);
	list.Add(2);
	list.Add(3);
	list.Add(4);
	list.Remove(1);
	list.Add(5);
	list.RemoveAllLesser(4);
	list.Add(10);
	int n = list.GetLargerCount(4);
	return 0;
}