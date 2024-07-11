#include <stdio.h>
#include <stdbool.h>

#define MAX 100

typedef struct {
    int priority;
    bool is_target;
} Document;

typedef struct {
    Document data[MAX];
    int front, rear;
} Queue;

void initQueue(Queue* q) {
    q->front = 0;
    q->rear = 0;
}

bool isEmpty(Queue* q) {
    return q->front == q->rear;
}

void enqueue(Queue* q, Document doc) {
    q->data[q->rear++] = doc;
}

Document dequeue(Queue* q) {
    return q->data[q->front++];
}

Document peek(Queue* q) {
    return q->data[q->front];
}

bool hasHigherPriority(Queue* q, int value) {
    for (int i = q->front; i < q->rear; i++) {
        if (q->data[i].priority > value) {
            return true;
        }
    }
    return false;
}

int solution(int* priorities, int length, int location) {
    int answer = 0;
    Queue que;
    initQueue(&que);

    for (int i = 0; i < length; i++) {
        Document doc;
        doc.priority = priorities[i];
        doc.is_target = (i == location);
        enqueue(&que, doc);
    }

    while (!isEmpty(&que)) {
        Document current = dequeue(&que);

        if (hasHigherPriority(&que, current.priority)) {
            enqueue(&que, current);
        } else {
            answer++;
            if (current.is_target) {
                break;
            }
        }
    }

    return answer;
}
