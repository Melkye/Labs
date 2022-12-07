using EightPuzzle;

var states = StatesGenerator.Generate(1);

int maxTimeInMs =  3 * 60 * 1000;
int maxDepthLdfs = 2048;

(var ldfsStats, var ldfsImprovedStats, var aStarStats) = SolverPrinter.Solve(states, maxTimeInMs, maxDepthLdfs);

var ldfsAvgStats = SolverPrinter.ComputeAverageSolutionStats(ldfsStats);
var ldfsImprovedAvgStats = SolverPrinter.ComputeAverageSolutionStats(ldfsImprovedStats);
var aStarAvgStats = SolverPrinter.ComputeAverageSolutionStats(aStarStats);

SolverPrinter.PrintAllProblemsStats(ldfsStats, ldfsImprovedStats, aStarStats);
SolverPrinter.PrintAverageSolutionStats(new List<(double, int, int, double)>() { ldfsAvgStats, ldfsImprovedAvgStats, aStarAvgStats });