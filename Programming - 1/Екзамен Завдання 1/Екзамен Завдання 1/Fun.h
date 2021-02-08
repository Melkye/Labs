#pragma once
#include <iostream>
#include <iomanip>
#include <ctime>

using namespace std;

int** MatrixGenerator(int n);
void MatrixPrinter(int** matrix, int n);
int** ZeroLost(int** matrix, int n);
void ZeroMaker(int** matrix, int n);