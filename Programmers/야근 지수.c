#include <stdio.h>
#include <stdlib.h>

void maxHeapify(int heap[], int heapSize, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < heapSize && heap[left] > heap[largest])
        largest = left;

    if (right < heapSize && heap[right] > heap[largest])
        largest = right;

    if (largest != i) {
        int temp = heap[i];
        heap[i] = heap[largest];
        heap[largest] = temp;
        maxHeapify(heap, heapSize, largest);
    }
}

void buildMaxHeap(int heap[], int heapSize) {
    for (int i = heapSize / 2 - 1; i >= 0; i--)
        maxHeapify(heap, heapSize, i);
}

int extractMax(int heap[], int* heapSize) {
    if (*heapSize <= 0)
        return 0;

    if (*heapSize == 1) {
        (*heapSize)--;
        return heap[0];
    }

    int root = heap[0];
    heap[0] = heap[*heapSize - 1];
    (*heapSize)--;
    maxHeapify(heap, *heapSize, 0);

    return root;
}

void insertHeap(int heap[], int* heapSize, int value) {
    (*heapSize)++;
    int i = *heapSize - 1;
    heap[i] = value;

    while (i != 0 && heap[(i - 1) / 2] < heap[i]) {
        int temp = heap[i];
        heap[i] = heap[(i - 1) / 2];
        heap[(i - 1) / 2] = temp;
        i = (i - 1) / 2;
    }
}

int solution(int n, int works[], int worksSize) {
    int answer = 0;
    int heap[worksSize];
    int heapSize = 0;

    int sum = 0;
    for (int i = 0; i < worksSize; i++) {
        sum += works[i];
    }

    if (sum < n) {
        return 0;
    }

    for (int i = 0; i < worksSize; i++) {
        insertHeap(heap, &heapSize, works[i]);
    }

    for (int i = 0; i < n; i++) {
        int value = extractMax(heap, &heapSize);
        if (value > 1) {
            insertHeap(heap, &heapSize, value - 1);
        }
    }

    for (int i = 0; i < heapSize; i++) {
        answer += heap[i] * heap[i];
    }

    return answer;
}
