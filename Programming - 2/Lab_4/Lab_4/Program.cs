using Shapes;

namespace Lab_4
{
    class Program
    {
        static void Main()
        {

            Square S1 = new Square();
            Square S2 = new Square(A: (0, 2), B: (2, 0), D: (-2, 0), C: (0, -2)); 
            Square S3 = new Square(S2);
            Square S4 = S2 + 5;
            Square S5 = S3 - 5;
            Square S6 = 10 + S5; // = S4
            Square S7 = S4 / S1;
            double area1 = S1.Area;
            double side5 = S5.Side;
            double perimeter7 = S7.Perimeter;
        }
    }
}
