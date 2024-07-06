#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int x, y, dist;
} Node;

typedef struct {
    Node* data;
    int front, rear, size, capacity;
} Queue;

Queue* createQueue(int capacity) {
    Queue* queue = (Queue*)malloc(sizeof(Queue));
    queue->capacity = capacity;
    queue->front = queue->size = 0;
    queue->rear = capacity - 1;
    queue->data = (Node*)malloc(queue->capacity * sizeof(Node));
    return queue;
}

int isFull(Queue* queue) {
    return (queue->size == queue->capacity);
}

int isEmpty(Queue* queue) {
    return (queue->size == 0);
}

void enqueue(Queue* queue, Node item) {
    if (isFull(queue)) return;
    queue->rear = (queue->rear + 1) % queue->capacity;
    queue->data[queue->rear] = item;
    queue->size++;
}

Node dequeue(Queue* queue) {
    if (isEmpty(queue)) return (Node){-1, -1, -1};
    Node item = queue->data[queue->front];
    queue->front = (queue->front + 1) % queue->capacity;
    queue->size--;
    return item;
}

void freeQueue(Queue* queue) {
    free(queue->data);
    free(queue);
}

int solution(int** maps, int row, int col) {
    bool visited[row][col];
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            visited[i][j] = false;
        }
    }

    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};

    Queue* q = createQueue(row * col);
    enqueue(q, (Node){0, 0, 1});
    visited[0][0] = true;

    while (!isEmpty(q)) {
        Node node = dequeue(q);
        int x = node.x, y = node.y, dist = node.dist;

        if (x == row - 1 && y == col - 1) {
            freeQueue(q);
            return dist;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < row && ny >= 0 && ny < col && !visited[nx][ny] && maps[nx][ny]) {
                visited[nx][ny] = true;
                enqueue(q, (Node){nx, ny, dist + 1});
            }
        }
    }

    freeQueue(q);
    return -1;
}
