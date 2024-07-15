#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int size;
    int count;
} Tangerine;

int compare_size(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int compare_count(const void *a, const void *b) {
    return ((Tangerine *)b)->count - ((Tangerine *)a)->count;
}

int solution(int k, int *tangerine, int tangerineSize) {
    int answer = 0;
    qsort(tangerine, tangerineSize, sizeof(int), compare_size);
    
    Tangerine *new = (Tangerine *)malloc(tangerineSize * sizeof(Tangerine));
    int newSize = 0;
    int cnt = 1;
    
    for (int i = 0; i < tangerineSize; i++) {
        if (i == tangerineSize - 1) {
            new[newSize].size = tangerine[i];
            new[newSize].count = cnt;
            newSize++;
        } else if (tangerine[i] == tangerine[i + 1]) {
            cnt++;
        } else {
            new[newSize].size = tangerine[i];
            new[newSize].count = cnt;
            newSize++;
            cnt = 1;
        }
    }
    
    qsort(new, newSize, sizeof(Tangerine), compare_count);
    
    int total = 0;
    for (int i = 0; i < newSize; i++) {
        total += new[i].count;
        answer++;
        
        if (total >= k) {
            free(new);
            return answer;
        }
    }
    
    free(new);
    return answer;
}
