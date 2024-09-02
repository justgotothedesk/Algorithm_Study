#include <stdio.h>
#include <stdlib.h>

int* solution(int* sequence, int sequence_size, int k) {
    int total = 0;
    int* result = (int*)malloc(2 * sizeof(int));

    for (int i = sequence_size - 1; i >= 0; i--) {
        total += sequence[i];
        if (total > k) {
            total -= sequence[--sequence_size];
        } else if (total == k) {
            while (i >= 1 && sequence[i - 1] == sequence[sequence_size - 1]) {
                i--;
                sequence_size--;
            }
            result[0] = i;
            result[1] = sequence_size - 1;
            return result;
        }
    }

    free(result);
  
    return NULL;
}
