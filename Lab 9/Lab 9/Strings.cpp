#include "Strings.h"
double Sum(string s)
{
	double sum = 0;
	string this_number = "";
	for (int i = 0; i < s.size(); i++)
	{
		if (s[i] != ' ') this_number.push_back(s[i]);
		if ((s[i] == ' ' || i == s.size() - 1) && !this_number.empty())
		{
			sum += stod(this_number);
			this_number = "";
		}
	}
	return sum;
}