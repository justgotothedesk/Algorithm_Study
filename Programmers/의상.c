#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int solution(char* clothes[][2], int clothesSize) {
    int answer = 1;

    struct CategoryNode {
        char* category;
        int count;
        struct CategoryNode* next;
    };

    struct CategoryNode* categories = NULL;

    struct CategoryNode* findCategory(struct CategoryNode* head, char* category) {
        struct CategoryNode* current = head;
        while (current != NULL) {
            if (strcmp(current->category, category) == 0) {
                return current;
            }
            current = current->next;
        }
        return NULL;
    }

    void insertCategory(struct CategoryNode** head, char* category) {
        struct CategoryNode* existingNode = findCategory(*head, category);
        if (existingNode) {
            existingNode->count++;
        } else {
            struct CategoryNode* newNode = (struct CategoryNode*)malloc(sizeof(struct CategoryNode));
            newNode->category = strdup(category);
            newNode->count = 1;
            newNode->next = *head;
            *head = newNode;
        }
    }

    for (int i = 0; i < clothesSize; i++) {
        insertCategory(&categories, clothes[i][1]);
    }

    struct CategoryNode* current = categories;
    while (current != NULL) {
        answer *= (current->count + 1);
        current = current->next;
    }

    current = categories;
    while (current != NULL) {
        struct CategoryNode* temp = current;
        current = current->next;
        free(temp->category);
        free(temp);
    }

    return answer - 1;
}
