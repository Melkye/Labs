#pragma once
#include <string>
using namespace std;

class StringContainer
{
private: 
	static string classLine;
	string instanceLine;
public:
	StringContainer(string line);
	static int StaticCharCount(char searchChar);
	int InstanceCharCount(char searchChar);
};

