using System.Diagnostics;

namespace EightPuzzle
{
    internal class LdfsImproved
    {
        private readonly long MAX_TIME_MILLISECONDS;

        private readonly int _maxDepth;
        private int _statesGenerated;
        private int _maxStatesInMemorySimultaneously;
        private bool _isSolved;

        private readonly List<int> _visitedStatesHashCodes;

        private readonly Stopwatch _stopwatch;
        private string _notFoundMessage;
        public LdfsImproved(int maxDepth, long maxTimeMilliseconds)
        {
            _maxDepth = maxDepth;
            MAX_TIME_MILLISECONDS = maxTimeMilliseconds;

            _statesGenerated = -1;
            _maxStatesInMemorySimultaneously = 0;
            _isSolved = false;

            _visitedStatesHashCodes = new();

            _notFoundMessage = string.Empty;
            _stopwatch = new();
        }

        public (long, int, int, bool) Solve(EightPuzzleBoardNode root, int currentDepth = 0)
        {
            if (currentDepth == 0)
            {
                _stopwatch.Start();
            }
            _statesGenerated++;
            int currentStateNumber = _statesGenerated;

            if (currentDepth > _maxStatesInMemorySimultaneously)
            {
                _maxStatesInMemorySimultaneously = currentDepth;
            }

            _visitedStatesHashCodes.Add(root.GetHashCode());

            Console.WriteLine($"State {currentStateNumber}");
            Console.WriteLine($"Depth {currentDepth}");
            Console.WriteLine(root);

            if (root.IsTargetStateReached)
            {
                _isSolved = true;
            }
            else if (currentDepth == _maxDepth)
            {
                Console.WriteLine("Max depth reached");
            }
            else
            {
                if (_stopwatch.ElapsedMilliseconds >= MAX_TIME_MILLISECONDS)
                {
                    _stopwatch.Stop();
                    _notFoundMessage = "-------------------------------------------------------Time exceeded-------------------------------------------------------";
                }
                else
                {
                    foreach (var move in root.AvailableMoves)
                    {
                        Console.WriteLine("---");
                        Console.WriteLine($"Child of {currentStateNumber}");
                        EightPuzzleBoardNode child = move.Invoke();
                        if (!_visitedStatesHashCodes.Contains(child.GetHashCode()))
                        {
                            Solve(child, currentDepth + 1);
                            if (_isSolved)
                            {
                                break;
                            }
                        }
                        else
                        {
                            Console.WriteLine($"State {_statesGenerated}");
                            Console.WriteLine($"Depth {currentDepth}");
                            Console.WriteLine("State visited");
                        }
                    }
                }
            }

            if (!_isSolved && currentDepth == 0)
            {
                if (_notFoundMessage == string.Empty)
                {
                    _notFoundMessage = "-------------------------------------------------------Max depth reached in all paths-------------------------------------------------------";
                }

                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine(_notFoundMessage);
                Console.ForegroundColor = ConsoleColor.White;
            }
            return (_stopwatch.ElapsedMilliseconds, _statesGenerated, _maxStatesInMemorySimultaneously, _isSolved);
        }
    }
}
