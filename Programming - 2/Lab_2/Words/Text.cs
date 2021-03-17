using System;

namespace Words
{
    public class Text
    {
		//public Text()
		//{
		//	_size = 0;
		//	_content = null;//??
		//}

		public Text(in CustomString[] array)
		{
			SetContent(array);
		}

        public void SetContent(CustomString[] array)
        {
            _size = array.Length;
            _content = new CustomString[_size];
            for (int i = 0; i < _size; i++)
                _content[i] = array[i];
        }
        public CustomString[] GetContent()
        {
            CustomString[] outContent = new CustomString[_size];
            for (int i = 0; i < _size; i++)
                outContent[i] = _content[i];
            return outContent;
            //return _content;
        }
        public int GetSize()
        {
            return _size;
        }

        public void AddRow(CustomString newRow)
		{
			_size++;
			CustomString[] tempText = new CustomString[_size];
			for (int i = 0; i < _size - 1; i++)
				tempText[i] = _content[i];
			tempText[_size - 1] = newRow;
			_content = tempText;
		}
        public void DeleteRow(int rowIndex)
        {
            CustomString[] newText = new CustomString[_size-1];
            for (int oldIndex = 0, newIndex = 0; newIndex < _size - 1; oldIndex++, newIndex++)
            {
                if (oldIndex == rowIndex)
                    oldIndex++;
                newText[newIndex] = _content[oldIndex];
            }
            _size--;
            SetContent(newText);
        }

        public void DeleteRow(CustomString searchedSubstring)  // deletes all rows containing a specified substring
        {
            //int nRowToDelete = 0;
            //bool isSubstringFound = false;
            char[] substring = searchedSubstring.GetString();
            for (int i = 0; i < _size; i++)
            {
                char[] textRow = _content[i].GetString();
                int substringIndex = 0;
                for (int j = 0; j < _content[i].GetLength(); j++)
                {
                    if (substring[substringIndex] == textRow[j])
                        substringIndex++;
                    else
                        substringIndex = 0;

                    if (substringIndex == substring.Length)
                    {
                        DeleteRow(i);
                        DeleteRow(searchedSubstring);
                        break;
                    }
                }
            }

            //if (isSubstringFound)
            //{
            //    DeleteRow(nRowToDelete);
            //}
        }

        public int LongestRow()
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
        public void SetUppercase()
        {
            for (int i = 0; i < _size; i++)
            {
                int tempStringSize = _content[i].GetLength();
                char[] tempString = _content[i].GetString();
                for (int j = 0; j < _content[i].GetLength(); j++)
                {
                    char checkChar = _content[i].GetString()[j];
                    if (char.IsLower(checkChar) && (j == 0 || _content[i].GetString()[j - 1] == ' '))
                    {
                        tempString[j] = (char)(Convert.ToInt32(checkChar) - 32);
                    }
                }
                _content[i] = new CustomString(tempString);
            }
        }
        public void Clear()
        {
            for (int i = 0; i < _size; i++)
            {
                _content[i].Clear();
            }
        }

        private CustomString[] _content;
		private int _size;
	}
}
