using Shapes;
using System;

namespace Lab_4
{
    class Program
    {
        static void Main()
        {

            Square S1 = new Square();
            Square S2;
            Square S3;
            Square S4;
            Square S5;
            Square S6;
            Square S7;
            try
            {
                S2 = new Square(A: (0, 2), B: (2, 0), D: (-2, 0), C: (0, -2));
                try
                {
                    S3 = new Square(S2);
                    try
                    {
                        S5 = S3 - 5;
                        try
                        {
                            S6 = 10 + S5; // = S4
                        }
                        catch (ArgumentException e)
                        {
                            Console.WriteLine(e.Message);
                        }
                    }
                    catch (ArgumentException e)
                    {
                        Console.WriteLine(e.Message);
                    }
                }
                catch (ArgumentException e)
                {
                    Console.WriteLine(e.Message);
                }
                try
                {
                    S4 = S2 + 5;
                    try
                    {
                        S7 = S4 / S1;
                    }
                    catch (ArgumentException e)
                    {
                        Console.WriteLine(e.Message);
                    }
                }
                catch (ArgumentException e)
                {
                    Console.WriteLine(e.Message);
                }
            }
            catch (ArgumentException e)
            {
                Console.WriteLine(e.Message);
            }
            //try
            //{
            //    S3 = new Square(S2);
            //}
            //catch (ArgumentException e)
            //{
            //    Console.WriteLine(e.Message);
            //}
            //try
            //{
            //    S4 = S2 + 5;
            //}
            //catch (ArgumentException e)
            //{
            //    Console.WriteLine(e.Message);
            //}
            //try
            //{
            //    S5 = S3 - 5;
            //}
            //catch (ArgumentException e)
            //{
            //    Console.WriteLine(e.Message);
            //}
            //try
            //{
            //    S6 = 10 + S5; // = S4
            //}
            //catch (ArgumentException e)
            //{
            //    Console.WriteLine(e.Message);
            //}
            //try
            //{
            //   S7 = S4 / S1;
            //}
            //catch (ArgumentException e)
            //{
            //    Console.WriteLine(e.Message);
            //}
        }
    }
}
