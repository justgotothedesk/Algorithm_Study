#include <stdio.h>
#include <string.h>

int answer = -1;
char big[] = {'A', 'E', 'I', 'O', 'U'};
char word[6];

int dfs(char* string) {
    answer++;
    
    if (strcmp(string, word) == 0) {
        return 1;
    }
    if (strlen(string) == 5) {
        return 0;
    }
    
    char new_string[6];
    
    for (int i = 0; i < 5; i++) {
        strcpy(new_string, string);
        int len = strlen(new_string);
        new_string[len] = big[i];
        new_string[len+1] = '\0';
        
        if (dfs(new_string)) {
            return 1;
        }
    }
    
    return 0;
}

int solution(char* input_word) {
    strcpy(word, input_word);
    answer = -1;
    
    char empty_string[1] = "";
    dfs(empty_string);
    
    return answer;
}
