using System;
using Symbols;

namespace Lab_3_CS
{
    class Program
    {
        static void Main()
        {
            char[] symbols = {'s', 'o', 'm', 'e', 'k', 'i', 'n', 'd',
                'o', 'f', 'w', 'o', 'r', 'd', 's'};
            CharArray theWord = new CharArray(symbols);
            int nVowels = theWord.NumberOfVowels;
            char first = theWord[0];
            theWord[0] = 1;
            nVowels = theWord.NumberOfVowels;
            theWord[22] = '5';
        }
    }
}
