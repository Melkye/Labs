using System;

namespace Arithmetics
{
    public class ArithmeticExpression
    {
        private int a;
        private int b;
        private int c;
        private int d;

        public ArithmeticExpression(int a, int b, int c, int d)
        {
            this.a = a;
            this.b = b;
            this.c = c;
            this.d = d;
        }

        public double Calculate()
        {
            double denom = a / 4 + c;
            double antilog = 2 * c - d;
            if (denom == 0)
                throw new DivideByZeroException("Attempt to divide by zero. a = -4c");
            if (antilog <= 0)
                throw new ArithmeticException("Attempt to take logarithm of a non-positive number. 2c = d");
            return (Math.Log10(antilog) + d - 152) / denom;
        }
    }
}
