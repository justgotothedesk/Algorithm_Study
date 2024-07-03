#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void dfs(int n, char** num, char* result) {
    char buffer[2];
    buffer[0] = num[n % 3][0];
    buffer[1] = '\0';
    strcat(result, buffer);
    if (n / 3 == 0) {
        return;
    }
    dfs(n / 3 - 1, num, result);
}

char* solution(int n) {
    char* answer = (char*)malloc(50 * sizeof(char));
    answer[0] = '\0';
    n -= 1;
    char* num[] = {"1", "2", "4"};
    dfs(n, num, answer);
    
    int len = strlen(answer);
    for (int i = 0; i < len / 2; ++i) {
        char temp = answer[i];
        answer[i] = answer[len - i - 1];
        answer[len - i - 1] = temp;
    }
    
    return answer;
}

int main() {
    int n = 10;
    char* result = solution(n);
    printf("Result: %s\n", result);
    free(result);
    return 0;
}
