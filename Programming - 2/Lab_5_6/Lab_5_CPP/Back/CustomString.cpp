#include "CustomString.h"

CustomString::CustomString()
{
	Length = 0;
	Line = new char[1];
	Line[0] = '\0';
}

CustomString::CustomString(char* line)
{
	SetLine(line);
}

CustomString::~CustomString()
{
	delete[] Line;
}

int CustomString::GetLength() { return Length; }

char* CustomString::GetLine()
{ 
	char* outLine = new char[Length + 1];
	for (int i = 0; i < Length + 1; i++)
		outLine[i] = Line[i];
	return  outLine; 
}

void CustomString::SetLine(char* line)
{
	if (Line != nullptr)
		delete[] Line;
	Length = 0;
	Line = new char[1];
	if (line != nullptr)
	{
		while (line[Length] != '\0') {
			Length++;
			delete[] Line;
			Line = new char[Length + 1];
			for (int i = 0; i < Length; i++) {
				Line[i] = line[i];
			}
		}
	}
	Line[Length] = '\0';
}