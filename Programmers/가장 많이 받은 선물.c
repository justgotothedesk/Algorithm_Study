#include <stdio.h>
#include <string.h>

#define MAX_FRIENDS 1000

int convert[MAX_FRIENDS];
int score[MAX_FRIENDS];
int graph[MAX_FRIENDS][MAX_FRIENDS];

int get_friend_index(char friends[MAX_FRIENDS][21], int num_friends, char *friends_name) {
	for (int i = 0; i < num_friends; i++) {
		if (strcmp(friends[i], friends_name) == 0) {
			return i;
		}
	}

	return -1;
}

int solution(char friends[MAX_FRIENDS][21], int num_friends, char gifts[MAX_FRIENDS], int num_gifts) {
	int answer = 0;

	for (int i = 0; i < num_friends; i++) {
		convert[i] = i;
		score[i] = 0;
	}

	memset(graph, 0, sizeof(graph));

	for (int i = 0; i < num_gifts; i++) {
		char give[21], receive[21];
		sscanf(gifts[i], "%s %s", give, receive);
		int give_idx = get_friend_index(friends, num_friends, give);
		int receive_idx = get_friend_index(friends, num_friends, receive);

		graph[give_idx][receive_idx] += 1;
		score[give_idx] += 1;
		score[receive_idx] -= 1;
	}

	for (int i = 0; i < num_friends; i++) {
		int temp = 0;
		for (int j = 0; j < num_friends; j++) {
			if (i == j) {
				continue;
			}
			if (graph[i][j] && graph[i][j] > graph[j][i]) {
				temp += 1;
			} else if (graph[i][j] == graph[j][i]) {
				if (score[i] > score[j]) {
					temp += 1;
				}
			}
		}

		if (temp > answer) {
			answer = temp;
		}
	}

	return answer;
}
