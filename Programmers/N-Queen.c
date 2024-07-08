#include <stdio.h>
#include <stdbool.h>

int answer = 0;

bool check(int* board, int x) {
    for (int i = 0; i < x; i++) {
        if (abs(board[x] - board[i]) == x - i) {
            return false;
        }
    }
    return true;
}

void dfs(int* board, bool* visited, int x, int n) {
    if (x == n) {
        answer++;
        return;
    }
    for (int y = 0; y < n; y++) {
        if (visited[y]) {
            continue;
        }
        board[x] = y;
        if (check(board, x)) {
            visited[y] = true;
            dfs(board, visited, x + 1, n);
            visited[y] = false;
        }
    }
}

int solution(int n) {
    answer = 0;
    int board[n];
    bool visited[n];
    for (int i = 0; i < n; i++) {
        visited[i] = false;
    }
    dfs(board, visited, 0, n);
    return answer;
}
