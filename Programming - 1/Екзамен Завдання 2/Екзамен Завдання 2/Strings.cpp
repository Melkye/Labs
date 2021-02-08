#include "Strings.h"

string* TextInput(int n_lines)
{
	string* a_text = new string[n_lines];
	for (int i = 0; i < n_lines; i++)
	{
		getline(cin, a_text[i]);
	}
	return a_text;
}

void TextPrinter(string* a_Text, int length)
{
	for (int i = 0; i < length; i++)
	{
		cout << a_Text[i] << endl;
	}
}

string* Repeatable(string* a_Text, int length)
{
	string this_string;
	string* a_Repeat = new string[length];
	string temp;
	bool repeat = false;
	for (int i = 0; i < length; i++)
	{
		this_string = a_Text[i];
		a_Repeat[i] = "";
		temp = "";
		for (int j = 0; j < this_string.length() - 2; j++)
		{
			temp.push_back(this_string[j]);
			if (temp[0] == this_string[j] && j != 0)
			{
				temp.push_back(this_string[j]);
				//repeat = true;
			}
			if (temp.length() > a_Repeat[i].length()) a_Repeat[i] = temp;

		}
		//if (temp.length() > a_Repeat[i].length()) a_Repeat[i] = temp;
	}
	return a_Repeat;
}
