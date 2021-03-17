using System;

namespace Lab_1___C_Sharp
{
    class Program
    {
        static void Main()
        {
            int number = 0;
            DecreaseByOne(ref number);
            bool areEqual = Equality(-8, 125);
        }

        static void DecreaseByOne(ref int number)
        {
            int mask = 1;
            while (mask != 0)
            {
                number ^= mask;
                mask &= number;
                mask <<= 1;
            }
        }

        static bool Equality(int n1, int n2)
        {
            if ((n1 ^ n2) == 0)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
    }
}
