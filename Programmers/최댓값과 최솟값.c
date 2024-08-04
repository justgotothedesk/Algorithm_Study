#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

void splitAndConvert(const char* s, int** arr, int* size) {
    char* token;
    char* str = strdup(s);
    char* rest = str;
    int* result = NULL;
    int count = 0;

    while ((token = strtok_r(rest, " ", &rest))) {
        result = (int*)realloc(result, sizeof(int) * (count + 1));
        result[count++] = atoi(token);
    }

    *arr = result;
    *size = count;
    free(str);
}

void findMinMax(int* arr, int size, int* min, int* max) {
    *min = INT_MAX;
    *max = INT_MIN;

    for (int i = 0; i < size; i++) {
        if (arr[i] < *min) {
            *min = arr[i];
        }
        if (arr[i] > *max) {
            *max = arr[i];
        }
    }
}

char* solution(const char* s) {
    int* arr = NULL;
    int size = 0;
    splitAndConvert(s, &arr, &size);

    int min, max;
    findMinMax(arr, size, &min, &max);

    // Allocate enough space for the result string
    char* answer = (char*)malloc(50 * sizeof(char));
    sprintf(answer, "%d %d", min, max);

    free(arr);
  
    return answer;
}
