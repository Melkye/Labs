using System;
using Words;

namespace Lab_2_CS
{
    class Program
    {
        static void Main()
        {
            int nRows1 = 0;
            Text firstText = new Text(EnterArrays.EnterStringArray(ref nRows1));
            PrintData.PrintText(firstText);
            Console.WriteLine("Enter a row to add to the end:");
            CustomString rowToAdd = new CustomString(EnterArrays.EnterCharArray());
            firstText.AddRow(rowToAdd);
            PrintData.PrintText(firstText);

            firstText.DeleteRow(0);
            Console.WriteLine("First line deleted.");
            PrintData.PrintText(firstText);

            firstText.SetUppercase();
            Console.WriteLine("First letters are uppercase.");
            PrintData.PrintText(firstText);

            Console.WriteLine("Enter a substring to delete:");
            CustomString substringToDelete = new CustomString(EnterArrays.EnterCharArray());
            firstText.DeleteRow(substringToDelete);
            PrintData.PrintText(firstText);

            int longest = firstText.LongestRow();
            firstText.Clear();
        }
    }

    class EnterArrays
    { 
        public static char[] EnterCharArray()
        {
            int length = 0;
            char[] array = new char[0];
            char tempChar = (char)Console.Read();
            while (tempChar != '\r')
            {
                char[] tempArray = new char[length + 1];
                for (int i = 0; i < length; i++)
                {
                    tempArray[i] = array[i];
                }
                tempArray[length] = tempChar;
                length++;
                array = tempArray;
                //tempArray = null;        //??
                tempChar = (char)Console.Read();
            }
            Console.Read();		// to ignore '\n'
            return array;
        }

        public static CustomString[] EnterStringArray(ref int nRows)
        {
            Console.Write("Enter the number of rows you want to write: ");
            nRows = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Enter the Text:");
            CustomString[] array = new CustomString[nRows];
            for (int i = 0; i < nRows; i++)
            {
                array[i] = new CustomString(EnterCharArray());
            }
            return array;
        }
    }
    class PrintData
    {
        public static void PrintText(Text text)
        {
            Console.WriteLine("Your text:");
            for (int i = 0; i < text.GetSize(); i++)
            {
                for (int j = 0; j < text.GetContent()[i].GetLength(); j++)
                {
                    Console.Write(text.GetContent()[i].GetString()[j]);
                }
                Console.Write('\n');
            }
            Console.WriteLine();
        }
    }
}
