#include "Lab2.h";

int main() {
	int nRows1 = 0;
	Text firstText(EnterStringArray(nRows1), nRows1);
	//PrintText(firstText);

	cout << "Enter a row to add to the end:" << endl;
	CustomString rowToAdd(EnterCharArray());
	firstText.AddRow(rowToAdd);
	//PrintText(firstText);

	firstText.DeleteRow(0);
	//PrintText(firstText);

	firstText.SetUppercase();
	//PrintText(firstText);

	cout << "Enter a substring to delete:" << endl;
	CustomString substringToDelete = CustomString(EnterCharArray());
	firstText.DeleteRow(substringToDelete);
	//PrintText(firstText);

	int longestRow = firstText.LongestRow();
	firstText.Clear();
	return 0;
}

char* EnterCharArray() {
	int length = 0;
	char* array = new char[1];
	char tempChar = cin.get();
	while (tempChar != '\n') {
		char* tempArray = new char[length + 2];
		for (int i = 0; i < length; i++)
		{
			tempArray[i] = array[i];
		}
		tempArray[length] = tempChar;
		length++;
		char* forDeletion = array;
		array = tempArray;
		delete[] forDeletion;
		tempArray = nullptr;		//??
		tempChar = cin.get();
	}
	array[length] = '\0';
	return array;
}

CustomString* EnterStringArray(int& nRows) {
	cout << "Enter the number of rows you want to write: ";
	cin >> nRows;
	cin.ignore(1, '/n');
	cout << "Enter the Text:" << endl;
	CustomString* array = new CustomString[nRows];
	for (int i = 0; i < nRows; i++) {
		array[i] = CustomString(EnterCharArray());
	}
	return array;
}

//void PrintText(Text text)
//{
//	cout << "Your text:" << endl;
//	for (int i = 0; i < text.GetSize(); i++)
//	{
//		for (int j = 0; j < text.GetContent()[i].GetLength(); j++)
//		{
//			cout << text.GetContent()[i].GetString()[j];
//		}
//		cout << '\n';
//	}
//}