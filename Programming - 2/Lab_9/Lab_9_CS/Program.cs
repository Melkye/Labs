using System;
using Symbols;
using Math = Arithmetic.Math;

namespace Lab_9_CS
{
    class Program
    {
        static void Main()
        {
            SomeDelegate symbolDelegate = StringContainer.StaticCharCount;
            StringContainer sc = new StringContainer("hello, abuba");
            int n;
            if (symbolDelegate != null)
                n = symbolDelegate('k');
            symbolDelegate -= StringContainer.StaticCharCount;
            symbolDelegate += sc.InstanceCharCount;
            if (symbolDelegate != null)
                n = symbolDelegate('a');

            Math.IntegerDivision += BadMathEventHandler;
            Math.IntegerDivision += GoodMathEventHandler;
            int a = Math.Add(2, 5);
            double b = Math.Divide(10, 2.5);
            int c = Math.Divide(10, 3);
            Console.WriteLine("ACHTUNG!");
        }

        static void BadMathEventHandler()
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("ACHTUNG!");
            Console.ForegroundColor = ConsoleColor.White;
        }
        static void GoodMathEventHandler()
        {
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("ACHTUNG!");
            Console.ForegroundColor = ConsoleColor.White;
        }
    }
}
