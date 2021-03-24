using System;

namespace Lab4
{
    class Program
    {
        static void Main()
        {
            double[,] matrix = { {6.48, 1.28, 0.79, 1.21},
                                  {1.28, 4.16, 1.3, 0.16},
                                  {0.79, 1.3, 5.66, 2.1},
                                  {1.21, 0.16, 2.1, 5.88}};
            Eigen.Computation.PrintMatrix(matrix, "  The Matrix:");
            matrix = Eigen.Computation.GetSimMatrixP(matrix);
            double[] polynomial = Eigen.Computation.GetPolynomial(matrix);
            Eigen.Computation.PrintCharacteristicEquation(polynomial);
            Console.ReadKey();
        }
    }
}
