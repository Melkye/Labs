using System;

namespace Shapes
{
    public abstract class Shape
    {
        public abstract double Perimeter { get; }
        public abstract double Area { get; }
        protected static double GetDistance((double x, double y) A, (double x, double y) B)
            => Math.Sqrt((A.x - B.x) * (A.x - B.x) + (A.y - B.y) * (A.y - B.y));
    }
}
