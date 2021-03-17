using System;

namespace Lab2_SLE1
{
    class Program
    {
        static void Main()
        {
            //double[,] matrix1 = { {3.81, 0.25, 1.28, 1.25},
            //                     {2.25, 1.32, 5.08, 0.49},
            //                     {5.31, 6.78, 0.98, 1.04},
            //                     {9.89, 2.45, 3.35, 2.28} };
            double[,] matrix1 = { {5.43, 1.12, 0.95, 1.32, 0.83},
                                 {1.12, 4.03, 2.12, 0.57, 0.91},
                                 {0.95, 2.12, 6.38, 1.29, 1.57},
                                 {1.32, 0.57, 1.29, 2.32, 1.25},
                                 {0.83, 0.91, 1.57, 1.25, 5.21} };
            //double[] vector1 = { 4.21, 6.97, 2.38, 10.98 };
            double[] vector1 = { 6.54, 3.21, 3.93, 6.25, 5.3 };
            SoLE system1 = new SoLE(matrix1, vector1);
            Console.WriteLine(" Input System:");
            system1.PrintSystem();
            system1.GaussianMethod();
            system1.evalResidual();
            system1.PrintSolution();
            Console.ReadKey();
        }
    }
    public class SoLE
    {
       public SoLE(double[,] matrix, double[] vector)
       {
            int order = matrix.GetLength(1);

            this.inputMatrix = new double[order, order];
            this.inputVector = new double[order];
            this.matrix = matrix;
            this.vector = vector;
            this.x = new double[order];
            this.residual = new double[order];
            for (int i = 0; i < order; i++)
            {
                x[i] = 0;
                residual[i] = 0;
                this.inputVector[i] = vector[i];
                for (int j =0; j < order; j++)
                {
                    this.inputMatrix[i, j] = matrix[i, j];
                }
            }
       }
        private double[,] inputMatrix;
        private double[,] matrix;
        private double[] inputVector;
        private double[] vector;
        private double[] x;
        private double[] residual;

        public void PrintSystem()
        {
            int order = matrix.GetLength(1);
            for (int i = 0; i < order; i++)
            {
                for (int j = 0; j < order; j++)
                {
                    Console.Write("{0, 11:f6}", matrix[i, j]);
                }
                Console.Write(" | {0, 10:f6}", vector[i]);
                Console.WriteLine();
            }
            Console.WriteLine();
        }
        public void PrintSolution()
        {
            int order = matrix.GetLength(1);
            Console.WriteLine(" The Solution:");
            for (int i = 0; i < order; i++)
            {
               Console.Write("{0, 10:f6}", x[i]);
            }
            Console.WriteLine("\n");

            Console.WriteLine(" The Residual Vector:");
            for (int i = 0; i < order; i++)
            {
                Console.WriteLine("{0, 25}", residual[i]);
            }
            Console.WriteLine();
        }
        public void GaussianMethod()
        {
            int order = matrix.GetLength(1);
            for (int k = 0; k < order; k++)
            {
                double divisor = matrix[k, k];
                for (int i = k; i < order; i++)
                {
                    matrix[k, i] /= divisor;
                }
                vector[k] /= divisor;
                for (int j = k+1; j < order; j++)
                {
                    double multip = matrix[j, k];
                    for (int t = k; t < order; t++)
                    {
                        matrix[j, t] -= multip * matrix[k, t];
                    }
                    vector[j] -= multip * vector[k];
                }
                Console.WriteLine(" Intermediate System Step {0}:", k+1);
                PrintSystem();
            }

            for (int i = order - 1; i >= 0; i--)
            {
                double substr = 0;
                for (int j = order - 1; j > i; j--)
                {
                    substr += matrix[i, j] * x[j];
                    matrix[i, j] = 0;
                }
                vector[i] -= substr;
                x[i] = vector[i];
            }
            Console.WriteLine(" The Final System:");
            PrintSystem();
        }

        public void evalResidual()
        {
            int order = matrix.GetLength(1);
            for (int i = 0; i < order; i++)
            {
                residual[i] += inputVector[i]; 
                for (int j = 0; j < order; j++)
                {
                    residual[i] -= inputMatrix[i, j] * x[j];
                }
            }
        }
    }
}
