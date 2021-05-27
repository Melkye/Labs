using System;
using Arithmetics;

namespace Lab_7
{
    class Program
    {
        static void Main()
        {
            Random r = new Random();
            ArithmeticExpression[] someMath = new ArithmeticExpression[100];
            double[] moreMath = new double[100];
            for (int i = 0; i < someMath.Length; i++)
            {
                someMath[i] = new ArithmeticExpression(r.Next(i), r.Next(i), r.Next(i), r.Next(i));
            }

            for (int i = 0; i < moreMath.Length; i++)
            {
                try
                {
                    moreMath[i] = someMath[i].Calculate();
                }
                catch (DivideByZeroException e)
                {
                    moreMath[i] = 0;
                    Console.WriteLine($"{i + 1,3}. Error. " + e.Message);
                    throw new DivideByZeroException("adad", e);
                }
                catch (ArithmeticException e)
                {
                    moreMath[i] = 1.1;
                    Console.WriteLine($"{i + 1,3}. Error. " + e.Message);
                }
                catch (Exception e)
                {
                    moreMath[i] = 2.2;
                    Console.WriteLine($"{i + 1,3}. Error. " + e.Message);
                }
            }
        }
    }
}
