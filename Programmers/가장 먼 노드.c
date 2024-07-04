#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int* data;
    int front;
    int rear;
    int size;
    int capacity;
} Queue;

Queue* createQueue(int capacity) {
    Queue* queue = (Queue*)malloc(sizeof(Queue));
    queue->capacity = capacity;
    queue->front = queue->size = 0;
    queue->rear = capacity - 1;
    queue->data = (int*)malloc(queue->capacity * sizeof(int));
  
    return queue;
}

int isFull(Queue* queue) {
    return (queue->size == queue->capacity);
}

int isEmpty(Queue* queue) {
    return (queue->size == 0);
}

void enqueue(Queue* queue, int item) {
    if (isFull(queue)) return;
    queue->rear = (queue->rear + 1) % queue->capacity;
    queue->data[queue->rear] = item;
    queue->size = queue->size + 1;
}

int dequeue(Queue* queue) {
    if (isEmpty(queue)) return -1;
    int item = queue->data[queue->front];
    queue->front = (queue->front + 1) % queue->capacity;
    queue->size = queue->size - 1;
    return item;
}

void freeQueue(Queue* queue) {
    free(queue->data);
    free(queue);
}

int solution(int n, int** edge, int edgeSize, int* edgeColSize) {
    int answer = 0;
    int** graph = (int**)malloc(n * sizeof(int*));
    int* graphSizes = (int*)malloc(n * sizeof(int));
    int* visited = (int*)calloc(n, sizeof(int));

    for (int i = 0; i < n; i++) {
        graph[i] = (int*)malloc(n * sizeof(int));
        graphSizes[i] = 0;
    }

    for (int i = 0; i < edgeSize; i++) {
        int u = edge[i][0] - 1;
        int v = edge[i][1] - 1;
        graph[u][graphSizes[u]++] = v;
        graph[v][graphSizes[v]++] = u;
    }

    Queue* queue = createQueue(n);
    enqueue(queue, 0);
    visited[0] = 1;

    while (!isEmpty(queue)) {
        int idx = dequeue(queue);
        for (int i = 0; i < graphSizes[idx]; i++) {
            int node = graph[idx][i];
            if (visited[node] == 0) {
                visited[node] = visited[idx] + 1;
                enqueue(queue, node);
            }
        }
    }

    int maxv = 0;
    for (int i = 0; i < n; i++) {
        if (visited[i] > maxv) {
            maxv = visited[i];
        }
    }

    for (int i = 1; i < n; i++) {
        if (visited[i] == maxv) {
            answer++;
        }
    }

    for (int i = 0; i < n; i++) {
        free(graph[i]);
    }
    free(graph);
    free(graphSizes);
    free(visited);
    freeQueue(queue);

    return answer;
}
