#pragma once

#include <iostream> // ???
using namespace std; /////////////////////////////
class CustomString
{
public:
	CustomString();
	//CustomString(bool inputFromConsole);
	CustomString(char* charArray);
	~CustomString();

	char* GetString();
	int GetLength();
	void Clear();

private:
	char* _string; // square brackets??
	int _length;

};

