using System;
using Lines;

namespace Lab_5_CS
{
    class Program
    {
        static void Main()
        {
            char[] word = { 'I', 'C', '-', '0', '1', ' ', 'o', 'n', 'e', ' ', 'l', 'o', 'v', 'e'};
            CustomString S1 = new CustomString(word);

            char[] nums = { '1', '2', '3' };
            CustomDigitString S2 = new CustomDigitString(nums);

            CustomDigitString D2 = new CustomDigitString();

            char[] mix = { 'I', 'C', '-', '0', '1'};
            S2.Flip();
            word[3] = '9';
        }
    }
}
