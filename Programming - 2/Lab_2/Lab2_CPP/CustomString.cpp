#include "CustomString.h"


	CustomString::CustomString() {
		_length = 0;
		_string = new char[1];
		_string[_length] = '\0';
	}

	CustomString::CustomString(char* charArray) {
		_length = 0;
		_string = new char[1];
		while (charArray[_length] != '\0') {
			_length++;
			delete[] _string;
			_string = new char[_length + 1];
			for (int i = 0; i < _length; i++) {
				_string[i] = charArray[i];
			}
		}
		_string[_length] = '\0';
	}

	CustomString::~CustomString() {
		//delete[] _string;
	}

	char* CustomString::GetString()
	{
		char* outString = new char[_length + 1];
		for (int i = 0; i < _length; i++)
			outString[i] = _string[i];
		outString[_length] = '\0';
		return outString;
		//return _string;
	}

	int CustomString::GetLength() {
		return _length;
	}

	void CustomString::Clear()
	{
		delete[] _string;
		_length = 0;
	}