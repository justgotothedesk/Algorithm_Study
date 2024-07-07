#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef struct {
    int dist;
    int x;
    int y;
    int dir;
} Node;

typedef struct {
    Node* data;
    int front, rear, size, capacity;
} PriorityQueue;

PriorityQueue* createQueue(int capacity) {
    PriorityQueue* queue = (PriorityQueue*)malloc(sizeof(PriorityQueue));
    queue->capacity = capacity;
    queue->front = queue->size = 0;
    queue->rear = capacity - 1;
    queue->data = (Node*)malloc(queue->capacity * sizeof(Node));
    return queue;
}

int isFull(PriorityQueue* queue) {
    return (queue->size == queue->capacity);
}

int isEmpty(PriorityQueue* queue) {
    return (queue->size == 0);
}

void enqueue(PriorityQueue* queue, Node item) {
    if (isFull(queue)) return;
    queue->rear = (queue->rear + 1) % queue->capacity;
    queue->data[queue->rear] = item;
    queue->size++;
}

Node dequeue(PriorityQueue* queue) {
    if (isEmpty(queue)) return (Node){INT_MAX, -1, -1, -1};
    Node minNode = queue->data[queue->front];
    int minIdx = queue->front;
    for (int i = 0; i < queue->size; i++) {
        int idx = (queue->front + i) % queue->capacity;
        if (queue->data[idx].dist < minNode.dist) {
            minNode = queue->data[idx];
            minIdx = idx;
        }
    }
    queue->data[minIdx] = queue->data[queue->front];
    queue->front = (queue->front + 1) % queue->capacity;
    queue->size--;
    return minNode;
}

void freeQueue(PriorityQueue* queue) {
    free(queue->data);
    free(queue);
}
