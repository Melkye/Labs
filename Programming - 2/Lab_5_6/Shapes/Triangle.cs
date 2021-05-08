using System;

namespace Shapes
{
    public sealed class Triangle : Shape
    {
        public Triangle((double x, double y) A, (double x, double y) B, (double x, double y) C)
        {
            if ((A.x == B.x && B.x == C.x) || (A.y == B.y && B.y == C.y))
            {
                throw new ArgumentException("Vertexes can't be on the same line");
            }
            VertexA = A;
            VertexB = B;
            VertexC = C;
        }

        public (double x, double y) VertexA { get; private set; }
        public (double x, double y) VertexB { get; private set; }
        public (double x, double y) VertexC { get; private set; }

        public double SideA => GetDistance(VertexB, VertexC);
        public double SideB => GetDistance(VertexA, VertexC);
        public double SideC => GetDistance(VertexA, VertexB);

        public override double Area 
            => Math.Sqrt((Perimeter / 2) * (Perimeter / 2 - SideA) * (Perimeter / 2 - SideB) * (Perimeter / 2 - SideC));
        public override double Perimeter => SideA + SideB + SideC;
    }
}
