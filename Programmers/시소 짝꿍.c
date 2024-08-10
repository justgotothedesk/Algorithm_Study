#include <stdio.h>
#include <stdlib.h>

#define MAX_WEIGHT 1000
#define MIN_WEIGHT 100

int solution(int weights[], int size) {
    int answer = 0;
    int temp[MAX_WEIGHT + 1] = {0};
    
    for (int i = 0; i < size; i++) {
        temp[weights[i]]++;
    }
  
    for (int i = MIN_WEIGHT; i <= MAX_WEIGHT; i++) {
        answer += temp[i] * (temp[i] - 1) / 2;
      
        if (i * 3 / 2 <= MAX_WEIGHT) {
            answer += temp[i] * temp[i * 3 / 2];
        }
        if (i * 2 <= MAX_WEIGHT) {
            answer += temp[i] * temp[i * 2];
        }
        if (i * 4 / 3 <= MAX_WEIGHT && i * 4 % 3 == 0) {
            answer += temp[i] * temp[i * 4 / 3];
        }
    }

    return answer;
}
