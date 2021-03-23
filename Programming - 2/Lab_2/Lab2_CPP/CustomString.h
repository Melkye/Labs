#pragma once

#include <iostream> // ???
using namespace std; /////////////////////////////
class CustomString
{
public:
	CustomString();
	CustomString(char* charArray);
	~CustomString();

	char* GetString();
	int GetLength();
	void Clear();

private:
	char* _string;
	int _length;

};

