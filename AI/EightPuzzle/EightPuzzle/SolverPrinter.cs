namespace EightPuzzle
{
    internal static class SolverPrinter
    {
        public static (List<(double, int, int, bool)>, List<(double, int, int, bool)>, List<(double, int, int, bool)>) Solve(List<int [,]> states, long maxTimeMilliseconds, int maxDepthLdfs)
        {
            List<(double time, int statesGenerated, int maxStatesInMemorySimultaneously, bool isSolved)> ldfsStats = new();
            List<(double time, int statesGenerated, int maxStatesInMemorySimultaneously, bool isSolved)> ldfsImprovedStats = new();
            List<(double time, int statesGenerated, int maxStatesInMemorySimultaneously, bool isSolved)> aStarStats = new();

            foreach (var state in states)
            {
                var root = new EightPuzzleBoardNode(state);

                Console.WriteLine("\n ------ new problem ----- \n");

                (double time, int statesGenerated, int maxStatesInMemorySimultaneously, bool isSolved) = SolveLdfs(root, maxTimeMilliseconds, maxDepthLdfs);
                ldfsStats.Add((time, statesGenerated, maxStatesInMemorySimultaneously, isSolved));

                (time, statesGenerated, maxStatesInMemorySimultaneously, isSolved) = SolveLdfsImproved(root, maxTimeMilliseconds, maxDepthLdfs);
                ldfsImprovedStats.Add((time, statesGenerated, maxStatesInMemorySimultaneously, isSolved));

                (time, statesGenerated, maxStatesInMemorySimultaneously, isSolved) = SolveAStar(state, maxTimeMilliseconds);
                aStarStats.Add((time, statesGenerated, maxStatesInMemorySimultaneously, isSolved));
            }
            return (ldfsStats, ldfsImprovedStats, aStarStats);
        }
        public static (double, int, int, bool) SolveLdfs(EightPuzzleBoardNode root, long maxTimeMilliseconds, int maxDepth = 32)
        {
            const int MILLISECONDS_IN_MINUTE = 60 * 1000;

            Console.WriteLine($"LDFS for {root.GetHashCode()}:");

            var ldfs = new Ldfs(maxDepth, maxTimeMilliseconds);

            (double time, int statesGenerated, int maxStatesInMemorySimultaneously, bool isSolved) = ldfs.Solve(root);

            return (time / MILLISECONDS_IN_MINUTE, statesGenerated, maxStatesInMemorySimultaneously, isSolved);
        }
        public static (double, int, int, bool) SolveLdfsImproved(EightPuzzleBoardNode root, long maxTimeMilliseconds, int maxDepth = 32)
        {
            const int MILLISECONDS_IN_MINUTE = 60 * 1000;

            Console.WriteLine($"LDFS (improved) for {root.GetHashCode()}:");

            var ldfs = new LdfsImproved(maxDepth, maxTimeMilliseconds);

            (double time, int statesGenerated, int maxStatesInMemorySimultaneously, bool isSolved) = ldfs.Solve(root);

            return (time / MILLISECONDS_IN_MINUTE, statesGenerated, maxStatesInMemorySimultaneously, isSolved);
        }

        public static (double, int, int, bool) SolveAStar(int[,] initialState, long maxTimeMilliseconds)
        {
            const int MILLISECONDS_IN_MINUTE = 60 * 1000;

            Console.WriteLine($"A* for { (new EightPuzzleBoardNode(initialState)).GetHashCode()}:");
            var aStar = new Astar(maxTimeMilliseconds);

            (double time, int statesGenerated, int maxStatesInMemorySimultaneously, bool isSolved) = aStar.Solve(initialState);
            
            return (time / MILLISECONDS_IN_MINUTE, statesGenerated, maxStatesInMemorySimultaneously, isSolved);
        }
        public static (double, int, int, double) ComputeAverageSolutionStats(List<(double, int, int, bool)> stats)
        {
            double avgTime = 0;
            int avgStatesGenerated = 0;
            int avgMaxStatesInMemorySimultaneously = 0;

            int solvedCount = 0;
            double avgSolved = 0;

            foreach ((double time, int statesGenerated, int maxStatesInMemorySimultaneously, bool isSolved) in stats)
            {
                if (isSolved)
                {
                    solvedCount++;
                    avgTime += time;
                    avgStatesGenerated += statesGenerated;
                    avgMaxStatesInMemorySimultaneously += maxStatesInMemorySimultaneously;
                }
            }
            if (solvedCount > 0)
            {
                avgSolved = (double)solvedCount / stats.Count;
                avgTime /= solvedCount;
                avgStatesGenerated /= solvedCount;
                avgMaxStatesInMemorySimultaneously /= solvedCount;
            }
            return (avgTime, avgStatesGenerated, avgMaxStatesInMemorySimultaneously, avgSolved);
        }
        public static void PrintAllProblemsStats(params List<(double, int, int, bool)> [] stats)
        {
            Console.WriteLine($"--------------------------------Stats for each problem--------------------------------");
            Console.WriteLine();
            Console.WriteLine($"{"N",2}|{"Algorithm",15}|{"Time (m)",15}|{"States generated",20}|{"Max states in memory simultaneously",40}|{"Solved?",10}");
            Console.WriteLine();

            string[] algoritms = { "LDFS","LDFS (improved)", "A*" };

            for (int i = 0; i < stats[0].Count; i++)
            {
                for (int j = 0; j < stats.Length; j++)
                {
                    (double time, int statesGenerated, int maxStatesInMemorySimultaneously, bool isSolved) = stats[j][i];
                    Console.WriteLine($"{i + 1,2}|{algoritms[j],15}|{time,15:F2}|{statesGenerated,20}|{maxStatesInMemorySimultaneously,40}|{isSolved,10}");
                }
                Console.WriteLine();
            }
        }
        public static void PrintAverageSolutionStats(List<(double, int, int, double)> stats)
        {
            Console.WriteLine($"--------------------------------Average stats for solved problems--------------------------------");
            Console.WriteLine();
            Console.WriteLine($"{"",3}{"Algorithm",15}|{"Avg time (m)",15}|{"Avg states generated",20}|{"Avg max states in memory simultaneously",40}|{"Solved (%)",10}");
            Console.WriteLine();
            string[] algoritms = { "LDFS", "LDFS (improved)", "A*" };
            int i = 0;
            foreach ((double avgTime, int avgStatesGenerated, int avgMaxStatesInMemorySimultaneously, double avgSolved) in stats)
            {
                Console.WriteLine($"{"",3}{algoritms[i],15}|{avgTime,15:F2}|{avgStatesGenerated,20}|{avgMaxStatesInMemorySimultaneously,40}|{avgSolved,10:p}");
                i++;
            }
        }
    }
}
