#include <stdio.h>

void hanoi(int src, int mid, int des, int n, int answer[][2], int* idx) {
    if (n == 1) {
        answer[*idx][0] = src;
        answer[*idx][1] = des;
        (*idx)++;
    } else {
        hanoi(src, des, mid, n - 1, answer, idx);
        hanoi(src, mid, des, 1, answer, idx);
        hanoi(mid, src, des, n - 1, answer, idx);
    }
}

void solution(int n, int answer[][2], int* answer_size) {
    *answer_size = 0;
    hanoi(1, 2, 3, n, answer, answer_size);
}
