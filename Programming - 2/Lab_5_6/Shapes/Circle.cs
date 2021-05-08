using System;

namespace Shapes
{
    public sealed class Circle : Shape
    {
        public Circle(double r, (double x, double y) c)
        {
            if (r <=0)
            {
                throw new ArgumentException("Radius must be positive", "r");
            }
            Radius = r;
            Center = c;
        }

        public double Radius { get; private set; }
        public (double x, double y) Center { get; private set; }
        public override double Area => Math.PI * Radius * Radius;
        public override double Perimeter => 2  * Math.PI * Radius;
    }
}
