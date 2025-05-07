#include <iostream>
using namespace std;

int totalSolutions = 0;

bool isSafe(int row, int col, int **board, int n) {
    // Check row and column
    for (int i = 0; i < n; i++) {
        if (board[row][i] == 1 || board[i][col] == 1) return false;
    }

    // Check diagonals
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (abs(row - i) == abs(col - j) && board[i][j] == 1)
                return false;
        }
    }

    return true;
}

void printSolution(int **board, int n) {
    cout << "Solution " << totalSolutions << ":\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << (board[i][j] ? "Q " : ". ");
        }
        cout << endl;
    }
    cout << endl;
}

void solveNQueens(int **board, int col, int n) {
    if (col == n) {
        totalSolutions++;
        printSolution(board, n);
        return;
    }

    for (int i = 0; i < n; i++) {
        if (isSafe(i, col, board, n)) {
            board[i][col] = 1;
            solveNQueens(board, col + 1, n);
            board[i][col] = 0; // Backtrack
        }
    }
}

int main() {
    int n;
    cout << "Enter the board size (n): ";
    cin >> n;

    int** board = new int*[n];
    for (int i = 0; i < n; i++) {
        board[i] = new int[n]();
    }

    solveNQueens(board, 0, n);

    cout << "Total number of solutions: " << totalSolutions << endl;

    // Clean up
    for (int i = 0; i < n; i++) {
        delete[] board[i];
    }
    delete[] board;

    return 0;
}
