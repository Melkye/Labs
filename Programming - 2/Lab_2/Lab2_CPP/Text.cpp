#include "Text.h"
#include <ctype.h>

Text::Text()
{
	_size = 0;
	_content = nullptr;
}

Text::Text(CustomString* array, int& rows)
{
	SetContent(array, rows);
}

Text::~Text() {
	delete[] _content;
}

void Text::SetContent(CustomString* array, int rows)
{
	_size = rows;
	_content = new CustomString[rows];
	for (int i = 0; i < rows; i++) {
		_content[i] = array[i];
	}
}

CustomString* Text::GetContent()
{
	CustomString* outContent = new CustomString[_size];
	for (int i = 0; i < _size; i++)
	{
		outContent[i] = CustomString(_content[i].GetString());
	}
	return outContent;
	//return _content;
}

int Text::GetSize()
{
	return _size;
}


void Text::AddRow(CustomString newRow) {
	_size++;
	CustomString* tempText = new CustomString[_size];
	for (int i = 0; i < _size - 1; i++) {
		tempText[i] = _content[i];
	}
	tempText[_size - 1] = newRow;
	CustomString* forDeletion = _content;
	_content = tempText;
	//delete forDeletion; // delete[] forDeletion;?
	tempText = nullptr;
}

void Text::DeleteRow(int rowIndex)
{
	CustomString* newContent = new CustomString[_size - 1];
	for (int oldIndex = 0, newIndex = 0; newIndex < _size - 1; oldIndex++, newIndex++)
	{
		if (oldIndex == rowIndex)
			oldIndex++;
		newContent[newIndex] = _content[oldIndex];
	}
	_size--;
	SetContent(newContent, _size);
}

void Text::DeleteRow(CustomString searchedSubstring)  // deletes all rows containing a specified substring
{
	//int nRowToDelete = 0;
	//bool isSubstringFound = false;
	char* substring = searchedSubstring.GetString();
	int substringLength = searchedSubstring.GetLength();
	for (int i = 0; i < _size; i++)
	{
		char* textRow = _content[i].GetString();
		int substringIndex = 0;
		for (int j = 0; j < _content[i].GetLength(); j++)
		{
			if (substring[substringIndex] == textRow[j])
				substringIndex++;
			else
				substringIndex = 0;

			if (substringIndex == substringLength)
			{
				DeleteRow(i);
				DeleteRow(searchedSubstring);
				break;
			}
		}
	}
}

 int Text::LongestRow()
{
	int maxLength = 0;
	for (int i = 0; i < _size; i++)
	{
		if (maxLength < _content[i].GetLength())
		{
			maxLength = _content[i].GetLength();
		}
	}
	return maxLength;
}

void Text::SetUppercase()
 {
	 for (int i = 0; i < _size; i++)
	 {
		 int tempStringSize = _content[i].GetLength();
		 char* tempString = _content[i].GetString();
		 for (int j = 0; j < tempStringSize; j++)
		 {
			 char checkChar = tempString[j];
			 //if (islower(checkChar) && (j == 0 || _content[i].GetString()[j - 1] == ' '))
			 //{
				// tempString[j] = (char)((int)checkChar - 32);
			 //}
			 if (j == 0)
			 {
				 if (islower(checkChar))
				 {
					 //tempString[j] = (char)((int)checkChar - 32);
					 tempString[j] = toupper(checkChar - 32);
				 }
			 }
			 else if (_content[i].GetString()[j - 1] == ' ')
			 {
				 tempString[j] = toupper(checkChar - 32);
			 }
		 }
		 _content[i] = CustomString(tempString);
	 }
 }
void Text::Clear()
 {
	 for (int i = 0; i < _size; i++)
	 {
		 _content[i].Clear();
	 }
	 _size = 0;
 }