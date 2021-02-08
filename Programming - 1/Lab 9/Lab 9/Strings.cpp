#include "Strings.h"
double Sum(string s)
{
	double sum = 0;
	string this_number = "";		 // тимчасове "слово", що будет перетворюватися в число
	for (int i = 0; i < s.size(); i++)
	{
		if (s[i] != ' ') this_number.push_back(s[i]);  // якщо зустріли символ - записуємо в наше "слово"
		if ((s[i] == ' ' || i == s.size() - 1)		// якщо наступний символ - пробіл, або нинішній  - останній у рядку
			&& !this_number.empty())				// і водночас у нас є, що додавати до суми
		{
			sum += stod(this_number);				// додаємо число
			this_number = "";						// звільнюємо "слово"
		}
	}
	return sum;
}