using System;

namespace Arithmetic
{
    public delegate void MathDelegate();
    public class Math
    {
        public static event MathDelegate IntegerDivision;
        private static void OnIntegerDivision()
        {
            if (IntegerDivision != null)
                IntegerDivision();
        }
        public static double Add(double x, double y)
        {
            return x + y;
        }
        public static int Add(int x, int y)
        {
            return x + y;
        }
        public static double Divide(double dividend, double divisor)
        {
            return dividend / divisor;
        }
        public static int Divide(int dividend, int divisor)
        {
            OnIntegerDivision();
            return dividend / divisor;
        }
    }
}
