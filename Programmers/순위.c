#include <stdio.h>
#include <stdlib.h>

int solution(int n, int results[][2], int resultsSize) {
    int answer = 0;
    int **graph = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; i++) {
        graph[i] = (int *)malloc(n * sizeof(int));
        for (int j = 0; j < n; j++) {
            graph[i][j] = -2;
        }
        graph[i][i] = 0;
    }
    
    for (int i = 0; i < resultsSize; i++) {
        int win = results[i][0] - 1;
        int lose = results[i][1] - 1;
        graph[win][lose] = 1;
        graph[lose][win] = -1;
    }
    
    for (int mid = 0; mid < n; mid++) {
        for (int start = 0; start < n; start++) {
            for (int end = 0; end < n; end++) {
                if (graph[start][mid] == 1 && graph[mid][end] == 1) {
                    graph[start][end] = 1;
                    graph[end][start] = -1;
                }
            }
        }
    }
    
    for (int i = 0; i < n; i++) {
        int flag = 1;
        for (int j = 0; j < n; j++) {
            if (graph[i][j] == -2) {
                flag = 0;
                break;
            }
        }
        if (flag) {
            answer++;
        }
    }
    
    for (int i = 0; i < n; i++) {
        free(graph[i]);
    }
    free(graph);
    
    return answer;
}
