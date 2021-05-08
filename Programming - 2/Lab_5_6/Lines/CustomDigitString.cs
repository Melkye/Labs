using System;

namespace Lines
{
    public class CustomDigitString : CustomString
    {
        public CustomDigitString()
        { }
        public CustomDigitString(char[] line)
        {
            Line = line;
        }
        /// <summary>
        /// Setter only adds digits to the line
        /// </summary>
        public new char[] Line
        {
            get => base.Line;


            set
            {
                char[] tempLine = new char[value.Length];
                int nOfNonDigits = 0;
                for (int i = 0, iTemp = 0; i < value.Length; i++, iTemp++)
                {
                    if (!Char.IsDigit(value[i]))
                    {
                        nOfNonDigits++;
                        iTemp--;
                        continue;
                    }
                    tempLine[iTemp] = value[i];
                }

                line = new char[value.Length - nOfNonDigits];
                for (int i = 0; i < line.Length; i++)
                {
                    line[i] = tempLine[i];
                }
            }
        }
        public void Flip()
        {
            char[] tempLine = new char[Length];
            for (int i = 0; i < Length; i++)
            {
                tempLine[i] = Line[Length - 1 - i];
            }
            Line = tempLine;
        }
    }
}
