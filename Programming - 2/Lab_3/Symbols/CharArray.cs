using System;

namespace Symbols
{
    public class CharArray
    {
        public CharArray(char[] data)
        {
            Data = data;
        }
        public char[] Data { get; set; }
        public char this[int index]
        {
            get
            {
                if (index < 0 || index > Data.Length - 1)
                    throw new ArgumentOutOfRangeException();
                return Char.ToUpper(Data[index]);
            }
            set
            {
                if (index < 0 || index > Data.Length - 1)
                    throw new ArgumentOutOfRangeException();
                Data[index] = value;
            }
        }

        public int NumberOfVowels
        {
            get
            {
                int numberOfVowels = 0;
                for (int i = 0; i < Data.Length; i++)
                {
                    if (Data[i] == 'a' || Data[i] == 'o' || Data[i] == 'u' ||
                        Data[i] == 'e' || Data[i] == 'i')
                        numberOfVowels++;
                }
                return numberOfVowels;
            }
        }
    }
}
