#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

bool check(int num) {
    if (num > 1) {
        for (int i = 2; i <= sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
    return false;
}

int solution(char* numbers) {
    int answer = 0;
    int visited[10000000] = {0};
    int length = strlen(numbers);
    
    for (int i = 1; i <= length; i++) {
        char* permutation = (char*)malloc((i + 1) * sizeof(char));
        int* chosen = (int*)calloc(length, sizeof(int));

        for (int j = 0; j < length; j++) {
            if (!chosen[j]) {
                chosen[j] = 1;
                permutation[0] = numbers[j];
                permutation[1] = '\0';
                int temp_num = atoi(permutation);
                if (!visited[temp_num] && check(temp_num)) {
                    visited[temp_num] = 1;
                    answer++;
                }
                chosen[j] = 0;
            }
        }
        free(permutation);
        free(chosen);
    }

    return answer;
}
