using System;

namespace Lab3_SLE2
{
    class Program
    {
        static void Main()
        {
            double[,] matrix1 = { {5.43, 1.12, 0.95, 1.32, 0.83},
                                 {1.12, 4.03, 2.12, 0.57, 0.91},
                                 {0.95, 2.12, 6.38, 1.29, 1.57},
                                 {1.32, 0.57, 1.29, 4.32, 1.25},
                                 {0.83, 0.91, 1.57, 1.25, 5.46} };
            double[] vector1 = { 6.54, 3.21, 3.93, 6.25, 5.3 };
            SoLE system1 = new SoLE(matrix1, vector1);
            Console.WriteLine(" The Input System:");
            system1.PrintSystem();
            system1.SystemManip();
            system1.IterativeMethod(0.0000001);
            Console.ReadKey();
        }
    }
    public class SoLE
    {
        public SoLE(double[,] matrix, double[] vector)
        {
            int order = matrix.GetLength(0);

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
                for (int j = 0; j < order; j++)
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
            int order = matrix.GetLength(0);
            for (int i = 0; i < order; i++)
            {
                for (int j = 0; j < order; j++)
                {
                    Console.Write("{0, 11:f7}", matrix[i, j]);
                }
                Console.Write(" | {0, 9:f7}", vector[i]);
                Console.WriteLine();
            }
            Console.WriteLine();
        }
        public void PrintSolution()
        {
            int order = matrix.GetLength(0);
            Console.WriteLine(" The Solution:");
            for (int i = 0; i < order; i++)
            {
                Console.Write("{0, 11:f7}", x[i]);
            }
            Console.WriteLine();
        }

        public void PrintResidual()
        {
            int order = matrix.GetLength(0);
            Console.WriteLine(" The Residual Vector:");
            for (int i = 0; i < order; i++)
            {
                Console.Write("{0, 11:f7}", residual[i]);
            }
            Console.WriteLine("\n");
        }

        public void SystemManip()
        {
            int order = matrix.GetLength(0);
            double divisor = matrix[0, 0];
            for (int i = 0; i < order; i++)
            {
                matrix[0, i] /= divisor;
            }
            vector[0] /= divisor;
            for (int j = 1; j < order; j++)
            {
                double multip = matrix[j, 0];
                for (int t = 0; t < order; t++)
                {
                    matrix[j, t] -= multip * matrix[0, t];
                }
                vector[j] -= multip * vector[0];
            }
            Console.WriteLine(" The System after 1 iteration of Gaussian Method:");
            PrintSystem();
        }

        public void EvalResidual()
        {
            int order = matrix.GetLength(0);
            for (int i = 0; i < order; i++)
            {
                residual[i] = 0;
                residual[i] += inputVector[i];
                for (int j = 0; j < order; j++)
                {
                    residual[i] -= inputMatrix[i, j] * x[j];
                }
            }
        }

        public void IterativeMethod(double eps)
        {
            int order = matrix.GetLength(0);
            double[] xPrev = new double[order];
            for (int i = 0; i < order; i++)
            {
                x[i] = vector[i]/matrix[i, i];
            }

            bool isPrecisionAchieved = false;
            int iterations = 0;
            do
            {
               for (int i = 0; i < order; i++)
               {
                    xPrev[i] = x[i];
                    double rowSum = 0;
                    for (int j = 0; j < order; j++)
                    {
                        if (i != j)
                        {
                            rowSum += matrix[i, j] * xPrev[j];
                        }
                    }
                    x[i] = (-rowSum + vector[i]) / matrix[i, i];
                    isPrecisionAchieved = Math.Abs(x[i] - xPrev[i]) < eps;
               }
                iterations++;
                Console.Write(" {0}.", iterations);
                PrintSolution();
                EvalResidual();
                PrintResidual();

            } while (!isPrecisionAchieved);
        }
    }
}