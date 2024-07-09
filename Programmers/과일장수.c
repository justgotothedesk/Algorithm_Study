#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int*)b - *(int*)a);
}

int solution(int k, int m, int* score, int scoreSize) {
    int answer = 0;
    
    qsort(score, scoreSize, sizeof(int), compare);

    int cnt = 0;
    int temp[m];
    
    for (int i = 0; i < scoreSize; i++) {
        temp[cnt++] = score[i];
        if (cnt == m) {
            int minVal = temp[0];
            for (int j = 1; j < m; j++) {
                if (temp[j] < minVal) {
                    minVal = temp[j];
                }
            }
            answer += minVal * m;
            cnt = 0;
        }
    }
    
    return answer;
}
