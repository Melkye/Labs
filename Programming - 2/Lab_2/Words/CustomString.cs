
namespace Words
{
    public class CustomString
    {
		public CustomString()
		{
			_length = 0;
			_string = new char[0];
		}

		public CustomString(char[] charArray)
		{
			_length = charArray.Length;
			_string = new char[_length];
			for (int i = 0; i < _length; i++)
			{
				_string[i] = charArray[i];
            }
		}

		public char[] GetString()
        {
            char[] outString = new char[_length];
            for (int i = 0; i < _length; i++)
                outString[i] = _string[i];
			return outString;
            //return _string;
        }
		public int GetLength()
		{
			return _length;
		}

		public void Clear()
        {
			_string = null;
			_length = 0;
        }
		

		private char[] _string;
		private int _length;
	}
}
