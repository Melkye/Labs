#include <cctype>
#include "CustomDigitString.h"

CustomDigitString::CustomDigitString() : CustomString::CustomString()
{ }

CustomDigitString::CustomDigitString(char* line)
{
	SetLine(line);
}

void CustomDigitString::SetLine(char* line)
{
	if (Line != nullptr)
		delete[] Line;
	Length = 0;
	Line = new char[1];
	int j = 0;
	while (line[j] != '\0')
	{
		if (isdigit(line[j]))
		{
			Length++;
			char* tempLine = new char[Length + 1];
			for (int i = 0; i < Length - 1; i++)
			{
				tempLine[i] = Line[i];
			}
			tempLine[Length - 1] = line[j];
			delete[] Line;
			Line = tempLine;
		}
		j++;
	}
	Line[Length] = '\0';
}

void CustomDigitString::Flip()
{
	char* tempLine = new char[Length + 1];
	for (int i = 0; i < Length; i++)
	{
		tempLine[i] = Line[Length - 1 - i];
	}
	tempLine[Length] = '\0';
	delete[] Line;
	Line = tempLine;
}