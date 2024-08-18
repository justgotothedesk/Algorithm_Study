#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define MAX_QUEUE_SIZE 10000
#define MAX_WORD_SIZE 10

typedef struct {
    char word[MAX_WORD_SIZE];
    int dist;
} QueueItem;

typedef struct {
    QueueItem items[MAX_QUEUE_SIZE];
    int front;
    int rear;
} Queue;

void initQueue(Queue *q) {
    q->front = 0;
    q->rear = 0;
}

bool isEmpty(Queue *q) {
    return q->front == q->rear;
}

void enqueue(Queue *q, QueueItem item) {
    q->items[q->rear++] = item;
}

QueueItem dequeue(Queue *q) {
    return q->items[q->front++];
}

int solution(char *begin, char *target, char words[][MAX_WORD_SIZE], int wordsSize) {
    Queue q;
    initQueue(&q);

    QueueItem startItem;
    strcpy(startItem.word, begin);
    startItem.dist = 0;
    enqueue(&q, startItem);

    bool visited[wordsSize];
    memset(visited, false, sizeof(visited));

    while (!isEmpty(&q)) {
        QueueItem currentItem = dequeue(&q);
        if (strcmp(currentItem.word, target) == 0) {
            return currentItem.dist;
        }

        for (int i = 0; i < wordsSize; i++) {
            if (!visited[i]) {
                int same = 0;
                for (int j = 0; j < strlen(words[i]); j++) {
                    if (currentItem.word[j] == words[i][j]) {
                        same++;
                    }
                }
                if (same == strlen(words[i]) - 1) {
                    visited[i] = true;
                    QueueItem newItem;
                    strcpy(newItem.word, words[i]);
                    newItem.dist = currentItem.dist + 1;
                    enqueue(&q, newItem);
                }
            }
        }
    }

    return 0;
}
