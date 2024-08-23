#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int solution(int n, int m, int section[], int section_count) {
    int answer = 0;

    int *wall = (int*)malloc(n * sizeof(int));
    memset(wall, 1, n * sizeof(int));

    for (int i = 0; i < section_count; i++) {
        wall[section[i] - 1] = 0;
    }

    for (int i = 0; i <= n - m; i++) {
        if (wall[i] == 0) {
            for (int j = 0; j < m; j++) {
                wall[i + j] = 1;
            }
            answer++;
        }
    }

    for (int i = n - m + 1; i < n; i++) {
        if (wall[i] == 0) {
            answer++;
            break;
        }
    }

    free(wall);
  
    return answer;
}
