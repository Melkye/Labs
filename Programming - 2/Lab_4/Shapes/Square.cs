using System;

namespace Shapes
{
    public class Square
    {
        public Square() { }
                                                     
        public Square(in Square copySquare) : this(copySquare.VertexA,
            copySquare.VertexB, copySquare.VertexC, copySquare.VertexD)
        { }

        ///<summary> 
        ///Enter data in order A-B-C-D or use named arguments 
        ///</summary>
        public Square((double x, double y) A, (double x, double y) B,
            (double x, double y) C, (double x, double y) D)
        {
            if (GetDistance(A, B) != GetDistance(B, C) || GetDistance(A, B) != GetDistance(C, D) ||
                GetDistance(A, B) != GetDistance(A, D) ||                                           // AB
                GetDistance(B, C) != GetDistance(C, D) || GetDistance(B, C) != GetDistance(A, D) || // BC
                GetDistance(C, D) != GetDistance(A, D))                                             // CD
                throw new ArgumentException("Sides are not equal");

            if (GetDistance(A, C) != GetDistance(B, D))
                throw new ArgumentException("Diagonals are not equal");

            if ((A.x == B.x && A.y == B.y) || (A.x == C.x && A.y == C.y) || (A.x == D.x && A.y == D.y) || // A
                (B.x == C.x && B.y == C.y) || (B.x == D.x && B.y == D.y) ||                               // B
                (C.x == D.x && C.y == D.y))                                                               // C
                throw new ArgumentException("Two vertexex can't be at the same point");

            VertexA = A;
            VertexB = B;
            VertexC = C;
            VertexD = D;
        }

        public (double x, double y) VertexA { get; private set; } = (1, 1);
        public (double x, double y) VertexB { get; private set; } = (1, -1);
        public (double x, double y) VertexC { get; private set; } = (-1, -1);
        public (double x, double y) VertexD { get; private set; } = (-1, 1);
        public double Side => GetDistance(VertexA, VertexB);
        public double Perimeter => 4 * Side;
        public double Area => Side * Side;
        private (double, double) Center
            => ((VertexA.x + VertexC.x) / 2, (VertexA.y + VertexC.y) / 2);

        public static Square operator +(Square baseSquare, double addedCoord)
            => new Square(A: (baseSquare.VertexA.x + addedCoord, baseSquare.VertexA.y + addedCoord),
              B: (baseSquare.VertexB.x + addedCoord, baseSquare.VertexB.y + addedCoord),
              C: (baseSquare.VertexC.x + addedCoord, baseSquare.VertexC.y + addedCoord),
              D: (baseSquare.VertexD.x + addedCoord, baseSquare.VertexD.y + addedCoord));

        public static Square operator +
            (double addedCoord, Square baseSquare)
            => baseSquare + addedCoord;

        public static Square operator -(Square baseSquare, double substrCoord)
            => new Square(A: (baseSquare.VertexA.x - substrCoord, baseSquare.VertexA.y - substrCoord),
              B: (baseSquare.VertexB.x - substrCoord, baseSquare.VertexB.y - substrCoord),
              C: (baseSquare.VertexC.x - substrCoord, baseSquare.VertexC.y - substrCoord),
              D: (baseSquare.VertexD.x - substrCoord, baseSquare.VertexD.y - substrCoord));

        public static Square operator /(Square leftSquare, Square rightSquare)
        {
            double newSide = GetDistance(leftSquare.Center, rightSquare.Center);
            return new Square(A: (newSide / 2, newSide / 2), B: (newSide / 2, -newSide / 2),
                C: (-newSide / 2, -newSide / 2), D: (-newSide / 2, newSide / 2));
        }

        private static double GetDistance((double x, double y) A, (double x, double y) B)
            => Math.Sqrt((A.x - B.x) * (A.x - B.x) + (A.y - B.y) * (A.y - B.y));
    }
}
