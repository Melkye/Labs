#pragma once
#include "CustomString.h"

class Text
{
public:
	Text();
	Text(CustomString* array, int& rows);
	~Text();
	void SetContent(CustomString* array, int rows);
	CustomString* GetContent();
	int GetSize();
	void AddRow(CustomString newRow);
	void DeleteRow(int rowIndex);
	void DeleteRow(CustomString searchedString); //deletes every row containing a specified substring
	int LongestRow();
	void SetUppercase();
	void Clear();
private:
	CustomString* _content;
	int _size;
};

