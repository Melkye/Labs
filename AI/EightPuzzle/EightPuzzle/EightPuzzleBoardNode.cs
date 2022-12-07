namespace EightPuzzle
{
    internal class EightPuzzleBoardNode
    {
        public static int[,] TargetState { get; } = {{1, 2, 3},
                                                     {4, 5, 6},
                                                     {7, 8, 0}};
        public (int i, int j) _blankCellPosition;

        public EightPuzzleBoardNode(int[,] initialState)
        {
            CurrentState = initialState;
            _blankCellPosition = FindBlankCellPosition();
            AvailableMoves = new();
            UpdateAvailableMoves();
        }

        public int[,] CurrentState { get; }
        public List<Func<EightPuzzleBoardNode>> AvailableMoves { get; }

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
            (int i, int j) = _blankCellPosition;
            if (i > 0)
            {
                AvailableMoves.Add(MoveBlankCellUp);
            }
            if (j < 2)
            {
                AvailableMoves.Add(MoveBlankCellRight);
            }
            if (i < 2)
            {
                AvailableMoves.Add(MoveBlankCellDown);
            }
            if (j > 0)
            {
                AvailableMoves.Add(MoveBlankCellLeft);
            }
        }
        private int [,] CopyState()
        {
            int [,] copyState = new int [3, 3];
            for (int i = 0; i < CurrentState.GetLength(0); i++)
            {
                for (int j = 0; j < CurrentState.GetLength(1); j++)
                {
                    copyState[i, j] = CurrentState[i, j];
                }
            }
            return copyState;
        }
        public virtual EightPuzzleBoardNode MoveBlankCellUp()
        {
            int[,] childNodeState = CopyState();

            (int i, int j) numberPosition = (_blankCellPosition.i - 1, _blankCellPosition.j);

            childNodeState[_blankCellPosition.i, _blankCellPosition.j] =
                childNodeState[numberPosition.i, numberPosition.j];

            childNodeState[numberPosition.i, numberPosition.j] = 0;

            return new EightPuzzleBoardNode(childNodeState);
        }
        public virtual EightPuzzleBoardNode MoveBlankCellDown()
        {
            int[,] childNodeState = CopyState();

            (int i, int j) numberPosition = (_blankCellPosition.i + 1, _blankCellPosition.j);

            childNodeState[_blankCellPosition.i, _blankCellPosition.j] =
                childNodeState[numberPosition.i, numberPosition.j];

            childNodeState[numberPosition.i, numberPosition.j] = 0;

            return new EightPuzzleBoardNode(childNodeState);
        }
        public virtual EightPuzzleBoardNode MoveBlankCellLeft()
        {
            int[,] childNodeState = CopyState();

            (int i, int j) numberPosition = (_blankCellPosition.i, _blankCellPosition.j - 1);

            childNodeState[_blankCellPosition.i, _blankCellPosition.j] =
                childNodeState[numberPosition.i, numberPosition.j];

            childNodeState[numberPosition.i, numberPosition.j] = 0;

            return new EightPuzzleBoardNode(childNodeState);
        }
        public virtual EightPuzzleBoardNode MoveBlankCellRight()
        {
            int[,] childNodeState = CopyState();

            (int i, int j) numberPosition = (_blankCellPosition.i, _blankCellPosition.j + 1);

            childNodeState[_blankCellPosition.i, _blankCellPosition.j] =
                childNodeState[numberPosition.i, numberPosition.j];

            childNodeState[numberPosition.i, numberPosition.j] = 0;

            return new EightPuzzleBoardNode(childNodeState);
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
                board += "\n";
            }
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
    }
}