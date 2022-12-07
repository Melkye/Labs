using System.Collections;

namespace EightPuzzle
{
    internal class EightPuzzleBoard : IEnumerable<int>
    {
        public static int[,] TargetState { get; } = {{1, 2, 3},
                                                     {4, 5, 6},
                                                     {7, 8, 0}};
        public (int i, int j) _blankCellPosition;

        public EightPuzzleBoard(int[,] initialState)
        {
            CurrentState = initialState;
            _blankCellPosition = FindBlankCellPosition();
            AvailableMoves = new();
            UpdateAvailableMoves();
        }

        public int[,] CurrentState { get; }
        public List<Action> AvailableMoves { get; } // possible problem when using: not known exactly what move is done
        public bool IsTargetStateReached
        {
            get
            {
                for (int i = 0; i < CurrentState.GetLength(0); i++)
                {
                    for (int j = 0; j < CurrentState.GetLength(1); j++)
                    {
                        if (CurrentState[i, j] != TargetState[i, j])
                        {
                            return false;
                        }
                    }
                }
                return true;
            }
        }
        private (int, int) FindBlankCellPosition()
        {
            for (int i = 0; i < CurrentState.GetLength(0); i++)
            {
                for (int j = 0; j < CurrentState.GetLength(1); j++)
                {
                    if (CurrentState[i, j] == 0)
                    {
                        return (i, j);
                    }
                }
            }
            return (0, 0);
        }
        private void UpdateAvailableMoves()
        {
            AvailableMoves.Clear();

            (int i, int j) = _blankCellPosition;
            if (i > 0)
            {
                AvailableMoves.Add(MoveBlankCellUp);
            }
            if (i < 2)
            {
                AvailableMoves.Add(MoveBlankCellDown);
            }
            if (j > 0)
            {
                AvailableMoves.Add(MoveBlankCellLeft);
            }
            if (j < 2)
            {
                AvailableMoves.Add(MoveBlankCellRight);
            }
        }
        public virtual void MoveBlankCellUp()
        {
            (int i, int j) numberPosition = (_blankCellPosition.i - 1, _blankCellPosition.j);

            CurrentState[_blankCellPosition.i, _blankCellPosition.j] =
                CurrentState[numberPosition.i, numberPosition.j];

            _blankCellPosition = numberPosition;
            CurrentState[_blankCellPosition.i, _blankCellPosition.j] = 0;

            UpdateAvailableMoves();
        }
        public virtual void MoveBlankCellDown()
        {
            (int i, int j) numberPosition = (_blankCellPosition.i + 1, _blankCellPosition.j);

            CurrentState[_blankCellPosition.i, _blankCellPosition.j] =
                CurrentState[numberPosition.i, numberPosition.j];

            CurrentState[numberPosition.i, numberPosition.j] = 0;

            UpdateAvailableMoves();
        }
        public virtual void MoveBlankCellLeft()
        {
            (int i, int j) numberPosition = (_blankCellPosition.i, _blankCellPosition.j - 1);

            CurrentState[_blankCellPosition.i, _blankCellPosition.j] =
                CurrentState[numberPosition.i, numberPosition.j];

            CurrentState[numberPosition.i, numberPosition.j] = 0;

            UpdateAvailableMoves();
        }
        public virtual void MoveBlankCellRight()
        {
            (int i, int j) numberPosition = (_blankCellPosition.i, _blankCellPosition.j + 1);

            CurrentState[_blankCellPosition.i, _blankCellPosition.j] =
                CurrentState[numberPosition.i, numberPosition.j];

            CurrentState[numberPosition.i, numberPosition.j] = 0;

            UpdateAvailableMoves();
        }
        public override string ToString()
        {
            string board = "";
            for (int i = 0; i < CurrentState.GetLength(0); i++)
            {
                for (int j = 0; j < CurrentState.GetLength(1); j++)
                {
                    board += CurrentState[i, j].ToString() + " ";
                }
                board.Trim();
                board += "\n";
            }
            board.Trim();
            return board;
        }

        public override int GetHashCode()
        {
            string numbers = "";
            for (int i = 0; i < CurrentState.GetLength(0); i++)
            {
                for (int j = 0; j < CurrentState.GetLength(1); j++)
                {
                    numbers += CurrentState[i, j].ToString();
                }
            }
            return int.Parse(numbers);
        }

        public IEnumerator<int> GetEnumerator()
        {
            for (int i = 0; i < CurrentState.GetLength(0); i++)
            {
                for (int j = 0; j < CurrentState.GetLength(1); j++)
                {
                    yield return CurrentState[i, j];
                }
            }
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }
    }
}
