using System;

namespace Lines
{
    public class CustomString
    {
        protected char[] line;
        public CustomString()
        {
            Line = new char[0];
        }
        public CustomString(char[] line)
        {
            Line = line;
        }

        public int Length => line.Length;
        public char [] Line
        {
            get
            {
                char[] outLine = new char[Length];
                for (int i = 0; i < Length; i++)
                    outLine[i] = Line[i];
                return outLine;
            }
            set
            {
                if (value == null)
                    throw new NullReferenceException("Array can't be null!");
                line = new char[value.Length];
                for (int i = 0; i < Length; i++)
                    line[i] = value[i];
            }
        }

    }
}
