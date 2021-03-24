//Computations.cs
using System;

namespace Eigen
{
    public static class Computation
    {
        public static double[,] GetInvMatrixM(double[,] matrixA, int i)
        {
            int order = matrixA.GetLength(0);
            double[,] invMatrixM = new double[order, order];
            for (int j = 0; j < order; j++)
            {
                invMatrixM[j, j] = 1;
                invMatrixM[(order - 2) - i, j] = matrixA[(order - 1) - i, j];
            }

            PrintMatrix(invMatrixM, "  Matrix M^-1({0})", order - i - 1);
            return invMatrixM;
        }
        public static double[,] GetMatrixM(double[,] matrixA, int i)
        {
            int order = matrixA.GetLength(0);
            double[,] matrixM = new double[order, order];
            for(int j = 0; j < order; j++)
            {
                matrixM[j, j] = 1;
                if (j == (order - 2) - i) // j = m - i
                {
                    matrixM[(order - 2) - i, j] = 1 / matrixA[(order - 1)- i, (order - 2) - i];
                }
                else
                {
                    matrixM[(order - 2) - i, j] = (-1) * matrixA[(order - 1) - i, j]
                        / matrixA[(order - 1) - i, (order - 2) - i];
                }
            }
            PrintMatrix(matrixM, "  Matrix M({0})", order - i - 1);
            return matrixM;
        }


        public static double[,] MatrixMultip(double[,] leftMatrix, double[,] rightMatrix)
        {
            int order = leftMatrix.GetLength(0);
            double[,] resultMatrix = new double[order, order];
            for (int i = 0; i < order; i++)
            {
                for (int j = 0; j < order; j++)
                {
                    resultMatrix[i, j] = 0;
                    for (int k = 0; k < order; k++)
                    resultMatrix[i,j] += leftMatrix[i, k] * rightMatrix[k, j];
                }
            }
            return resultMatrix;
        }

        public static double[,] GetSimMatrixP(double[,] matrixA)
        {
            int order = matrixA.GetLength(0);
            for (int i = 0; i < order - 1; i++)
            {
                double[,] invMatrixM = GetInvMatrixM(matrixA, i);
                double[,] matrixM = GetMatrixM(matrixA, i);
                matrixA = MatrixMultip(invMatrixM, matrixA);
                matrixA = MatrixMultip(matrixA, matrixM);
            }
            PrintMatrix(matrixA, "  Matrix P:");
            return matrixA;
        }

        public static double[] GetPolynomial(double[,] matrixP)
        {
            int order = matrixP.GetLength(0);
            double[] polynomial = new double[order + 1];
            for(int i = 0, m = order - 1; i < order; i++, m--)
            {
                polynomial[i] = -matrixP[0, m];
            }
            polynomial[order] = 1;
            return polynomial;
        }

        public static void PrintMatrix(double[,] matrix, string text)
        {
            int order = matrix.GetLength(0);
            Console.WriteLine(text);
            for (int i = 0; i < order; i++)
            {
                for (int j = 0; j < order; j++)
                {
                    Console.Write("{0, 12:f5}", matrix[i, j]);
                }
                Console.WriteLine();
            }
            Console.WriteLine();
        }
        public static void PrintMatrix(double[,] matrix, string text, int iter)
        {
            int order = matrix.GetLength(0);
            Console.WriteLine(text, iter);
            for (int i = 0; i < order; i++)
            {
                for (int j = 0; j < order; j++)
                {
                    Console.Write("{0, 12:f5}", matrix[i, j]);
                }
                Console.WriteLine();
            }
            Console.WriteLine();
        }

        public static void PrintCharacteristicEquation(double[] polynomial)
        {
            int size = polynomial.GetLength(0);
            Console.WriteLine("  The Characteristic Equation:");
            for (int i = size - 1; i >= 0; i--)
            {
                Console.Write("{0, 10:f5}*x^{1}", polynomial[i], i);
                if (i!=0 && polynomial[i] < 0)
                    Console.Write(" +");
            }
            Console.Write(" = 0");
            Console.WriteLine();

        }
    }
}
