#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

void to_lowercase(char *str) {
    while (*str) {
        *str = tolower(*str);
        str++;
    }
}

int create_bigrams(char *str, char bigrams[][3], int *count) {
    int len = strlen(str);
    *count = 0;

    for (int i = 0; i < len - 1; i++) {
        if (isalpha(str[i]) && isalpha(str[i + 1])) {
            bigrams[*count][0] = str[i];
            bigrams[*count][1] = str[i + 1];
            bigrams[*count][2] = '\0';
            (*count)++;
        }
    }
    return *count;
}

int solution(char *str1, char *str2) {
    int answer = 0;
    char A[1000][3];
    char B[1000][3];
    int countA = 0, countB = 0;
    int hap, kyo = 0;

    to_lowercase(str1);
    to_lowercase(str2);

    create_bigrams(str1, A, &countA);
    create_bigrams(str2, B, &countB);

    if (countA == 0 && countB == 0) {
        return 65536;
    }

    hap = countA + countB;

    for (int i = 0; i < countA; i++) {
        for (int j = 0; j < countB; j++) {
            if (strcmp(A[i], B[j]) == 0) {
                kyo++;
                for (int k = j; k < countB - 1; k++) {
                    strcpy(B[k], B[k + 1]);
                }
                countB--;
                hap--;
                break;
            }
        }
    }

    answer = (int)((double)kyo / hap * 65536);

    return answer;
}
