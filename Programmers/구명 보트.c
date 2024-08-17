#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int solution(int people[], int people_count, int limit) {
    int answer = 0;
  
    qsort(people, people_count, sizeof(int), compare);

    int left = 0;              
    int right = people_count - 1;

    while (left <= right) {
        if (left == right) {
            answer++;
            break;
        }
        if (people[left] + people[right] <= limit) {
            left++;
            right--;
        } else {
            right--;
        }
        answer++;
    }

    return answer;
}
