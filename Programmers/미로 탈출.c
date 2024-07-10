#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define MAX 1000 // Assume the maximum size of the map is 1000x1000

typedef struct {
    int x, y, cost;
} QueueNode;

typedef struct {
    QueueNode nodes[MAX * MAX];
    int front, rear;
} Queue;

void initQueue(Queue* q) {
    q->front = 0;
    q->rear = 0;
}

bool isEmpty(Queue* q) {
    return q->front == q->rear;
}

void enqueue(Queue* q, int x, int y, int cost) {
    q->nodes[q->rear].x = x;
    q->nodes[q->rear].y = y;
    q->nodes[q->rear].cost = cost;
    q->rear++;
}

QueueNode dequeue(Queue* q) {
    return q->nodes[q->front++];
}

int bfs(char start, char end, char** maps, int row, int col) {
    int dx[] = {1, -1, 0, 0};
    int dy[] = {0, 0, 1, -1};
    bool visited[row][col];
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            visited[i][j] = false;
        }
    }

    Queue q;
    initQueue(&q);
    bool check = false;

    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            if (maps[i][j] == start) {
                check = true;
                visited[i][j] = true;
                enqueue(&q, i, j, 0);
                break;
            }
        }
        if (check) break;
    }

    while (!isEmpty(&q)) {
        QueueNode node = dequeue(&q);
        int i = node.x;
        int j = node.y;
        int cost = node.cost;

        if (maps[i][j] == end) {
            return cost;
        }

        for (int c = 0; c < 4; c++) {
            int x = i + dx[c];
            int y = j + dy[c];

            if (0 <= x && x < row && 0 <= y && y < col && maps[x][y] != 'X' && !visited[x][y]) {
                visited[x][y] = true;
                enqueue(&q, x, y, cost + 1);
            }
        }
    }
    return -1;
}

int solution(char** maps, int row, int col) {
    int answer = 0;
    int first = bfs('S', 'L', maps, row, col);
    int second = bfs('L', 'E', maps, row, col);

    if (first != -1 && second != -1) {
        answer = first + second;
    } else {
        answer = -1;
    }

    return answer;
}
