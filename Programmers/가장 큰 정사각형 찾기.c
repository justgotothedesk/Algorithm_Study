#include <stdio.h>

int solution(int** board, int boardSize, int* boardColSize) {
    int answer = 0;

    if (boardSize == 1) {
        for (int j = 0; j < boardColSize[0]; j++) {
            if (board[0][j]) {
                return 1;
            }
        }
        return 0;
    }

    for (int i = 1; i < boardSize; i++) {
        for (int j = 1; j < boardColSize[i]; j++) {
            if (board[i][j]) {
                int min_val = board[i-1][j];
                if (board[i][j-1] < min_val) {
                    min_val = board[i][j-1];
                }
                if (board[i-1][j-1] < min_val) {
                    min_val = board[i-1][j-1];
                }
                board[i][j] = min_val + 1;
                if (board[i][j] > answer) {
                    answer = board[i][j];
                }
            }
        }
    }

    return answer * answer;
}
