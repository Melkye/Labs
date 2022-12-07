using System.Diagnostics;

namespace EightPuzzle
{
    internal class Astar
    {
        private readonly long MAX_TIME_MILLISECONDS;

        private int _statesGenerated;
        private int _maxStatesInMemorySimultaneously;
        private List<EightPuzzleBoardNode> _openStates;
        private readonly List<int> _visitedStatesHashCodes;
        private bool _isSolved;

        public Astar(long maxTimeMilliseconds)
        {
            MAX_TIME_MILLISECONDS = maxTimeMilliseconds;

            _statesGenerated = 0;
            _maxStatesInMemorySimultaneously = 0;
            _openStates = new();
            _visitedStatesHashCodes = new();
            _isSolved = false;
        }

        public (long, int, int, bool) Solve(int[,] initialState)
        {
            Stopwatch stopwatch = new();
            stopwatch.Start();

            EightPuzzleBoardNode root = new(initialState);
            _openStates.Add(root);
            int currentDepth = 0;

            Dictionary<int, int> gValues = new(); // key is GetHashCode(), value is node's depth
            gValues.Add(root.GetHashCode(), currentDepth);

            Dictionary<int, int> fValues = new();
            fValues.Add(root.GetHashCode(), ComputeHeuristic(initialState, EightPuzzleBoardNode.TargetState));

            while (_openStates.Count > 0)
            {
                if (stopwatch.ElapsedMilliseconds >= MAX_TIME_MILLISECONDS)
                {
                    stopwatch.Stop();
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("-------------------------------------------------------Time exceeded-------------------------------------------------------");
                    Console.ForegroundColor = ConsoleColor.White;
                    return (stopwatch.ElapsedMilliseconds, _statesGenerated, _maxStatesInMemorySimultaneously, _isSolved);
                }
                EightPuzzleBoardNode currentNode = _openStates.Last(); // because dict is sorted
                _visitedStatesHashCodes.Add(currentNode.GetHashCode());

                Console.WriteLine("---");
                Console.WriteLine($"State visited: {_visitedStatesHashCodes.Count}");
                Console.WriteLine(currentNode.ToString());

                if (currentNode.IsTargetStateReached)
                {
                    stopwatch.Stop();
                    _isSolved = true;
                    return (stopwatch.ElapsedMilliseconds, _statesGenerated, _maxStatesInMemorySimultaneously, _isSolved);
                }

                _openStates.Remove(currentNode);

                foreach (var move in currentNode.AvailableMoves)
                {
                    EightPuzzleBoardNode child = move.Invoke();

                    _statesGenerated++;
                    Console.WriteLine($"State generated: {_statesGenerated}");

                    int childGValueThroughCurrent = gValues[currentNode.GetHashCode()] + 1;
                    bool childGValueExists = gValues.TryGetValue(child.GetHashCode(), out int childGValueExisting);
                    if (!childGValueExists)
                    {
                        childGValueExisting = int.MaxValue;
                    }

                    if (childGValueThroughCurrent < childGValueExisting)
                    {
                        gValues[child.GetHashCode()] = childGValueThroughCurrent;
                        fValues[child.GetHashCode()] = childGValueThroughCurrent + ComputeHeuristic(child.CurrentState, EightPuzzleBoardNode.TargetState);
                        if (!_openStates.Contains(child))
                        {
                            _openStates.Add(child);
                        }
                    }
                }

                if (_openStates.Count > _maxStatesInMemorySimultaneously)
                {
                    _maxStatesInMemorySimultaneously = _openStates.Count;
                }

                _openStates = _openStates.OrderByDescending(node => fValues[node.GetHashCode()]).ToList();
            }
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("-------------------------------------------------------Traversal error-------------------------------------------------------");
            Console.ForegroundColor = ConsoleColor.White;
            stopwatch.Stop();
            return (stopwatch.ElapsedMilliseconds, _statesGenerated, _maxStatesInMemorySimultaneously, _isSolved);
        }

        private static int ComputeHeuristic(int[,] currentState, int[,] targetState)
        {
            int placedWrong = 8;

            for (int i = 0; i < currentState.GetLength(0); i++)
            {
                for (int j = 0; j < currentState.GetLength(1); j++)
                {
                    if (currentState[i, j] == targetState[i, j] && currentState[i, j] != 0)
                    {
                        placedWrong--;
                    }
                }
            }
            return placedWrong;
        }
    }
}
