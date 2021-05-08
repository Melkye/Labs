using System;
using Lines;

namespace Lab_5_CS
{
    class Program
    {
        static void Main()
        {
            char[] word = { 'q', 'u', 'e', 's', 't', 'i', 'o', 'n', 's', '?' };
            CustomString S1 = new CustomString(word);

            char[] nums = { '1', '2', '3' };
            CustomDigitString S2 = new CustomDigitString(nums);

            CustomDigitString D2 = new CustomDigitString();

            char[] mix = { 'q', 'u', '1', 'e', '2', 's'};
            S2.Flip();
            word[0] = 'A';
        }
    }
}
