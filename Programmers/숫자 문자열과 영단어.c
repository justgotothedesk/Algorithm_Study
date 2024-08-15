#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int convertWordToDigit(char *word) {
    if (strcmp(word, "zero") == 0) return 0;
    if (strcmp(word, "one") == 0) return 1;
    if (strcmp(word, "two") == 0) return 2;
    if (strcmp(word, "three") == 0) return 3;
    if (strcmp(word, "four") == 0) return 4;
    if (strcmp(word, "five") == 0) return 5;
    if (strcmp(word, "six") == 0) return 6;
    if (strcmp(word, "seven") == 0) return 7;
    if (strcmp(word, "eight") == 0) return 8;
    if (strcmp(word, "nine") == 0) return 9;
    return -1;
}

int solution(const char *s) {
    char answer[50] = "";
    char temp[10] = "";
    int answerIndex = 0;

    for (int i = 0; i < strlen(s); i++) {
        if (isalpha(s[i])) {
            strncat(temp, &s[i], 1);
            int digit = convertWordToDigit(temp);
            if (digit != -1) {
                answer[answerIndex++] = '0' + digit;
                temp[0] = '\0';
            }
        } else {
            answer[answerIndex++] = s[i];
        }
    }

    if (strlen(temp) > 0) {
        int digit = convertWordToDigit(temp);
        if (digit != -1) {
            answer[answerIndex++] = '0' + digit;
        }
    }

    answer[answerIndex] = '\0';

    return atoi(answer);
}

int main() {
    const char *input = "one4seveneight";
    int result = solution(input);
    printf("%d\n", result);
    return 0;
}
