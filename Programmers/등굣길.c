#include <stdio.h>
#include <stdlib.h>

#define MOD 1000000007

int solution(int m, int n, int **puddles, int puddlesSize, int *puddlesColSize) {
    int **maps = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; i++) {
        maps[i] = (int *)calloc(m, sizeof(int));
    }
    
    for (int i = 0; i < puddlesSize; i++) {
        int x = puddles[i][0];
        int y = puddles[i][1];
        maps[y - 1][x - 1] = -1; 
    }
    
    for (int i = 0; i < m; i++) {
        if (maps[0][i] == -1) break;
        maps[0][i] = 1;
    }
    
    for (int i = 0; i < n; i++) {
        if (maps[i][0] == -1) break;
        maps[i][0] = 1;
    }
    
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < m; j++) {
            if (maps[i][j] == -1) continue;
            
            if (maps[i - 1][j] != -1) {
                maps[i][j] = (maps[i][j] + maps[i - 1][j]) % MOD;
            }
            if (maps[i][j - 1] != -1) {
                maps[i][j] = (maps[i][j] + maps[i][j - 1]) % MOD;
            }
        }
    }
    
    int answer = maps[n - 1][m - 1] % MOD;
    
    for (int i = 0; i < n; i++) {
        free(maps[i]);
    }
    free(maps);
    
    return answer;
}
