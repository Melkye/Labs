namespace EightPuzzle
{
    internal static class StatesGenerator
    {
        public static List<int[,]> Generate(int n)
        {
            var states = new List<int[,]>(n);
            for (int i = 0; i < n; i++)
            {
                var state = GenerateOneState();
                states.Add(state);
            }
            return states;
        }
        private static int[,] GenerateOneState()
        {
            int[] stateFlatten;
            int inversionsNumber;
            do
            {
                stateFlatten = GenerateOneStateFlatten();
                inversionsNumber = CountInversions(stateFlatten);
            }
            while (inversionsNumber % 2 == 1);

            int [,] state = new int[3,3];

            for (int i = 0, k = 0; i < state.GetLength(0); i++)
            {
                for (int j = 0; j < state.GetLength(1); j++, k++)
                {
                    state[i, j] = stateFlatten[k];
                }
            }
            return state;
        }
        private static int[] GenerateOneStateFlatten()
        {
            Random random = new();

            int[] numbers = { 1, 2, 3, 4, 5, 6, 7, 8, 0 };

            int n = numbers.Length;
            while (n > 1)
            {
                n--;
                int i = random.Next(n + 1);

                int value = numbers[i];
                numbers[i] = numbers[n];
                numbers[n] = value;
            }
            return numbers;
        }

        private static int CountInversions(int[] numbers)
        {
            int count = 0;
            for (int i = 0; i < numbers.Length; i++)
            {
                for (int j = i + 1; j < numbers.Length; j++)
                {
                    if (numbers[i] > numbers[j] && numbers[i] != 0 && numbers[j] != 0)
                    {
                        count++;
                    }
                }
            }
            return count;
        }
    }
}
