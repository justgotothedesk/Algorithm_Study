#include <stdio.h>
#include <limits.h>

int convert(int x, int y, int sx, int sy, int m, int n) {
    int maxv = INT_MAX;

    int one = (sx + x) * (sx + x) + (y - sy) * (y - sy);
    if (y == sy && sx > x) {
        one = maxv;
    }

    int four = (sy - y) * (sy - y) + (2 * m - x - sx) * (2 * m - x - sx);
    if (y == sy && x > sx) {
        four = maxv;
    }

    int two = (sy + y) * (sy + y) + (sx - x) * (sx - x);
    if (x == sx && y < sy) {
        two = maxv;
    }

    int three = (sx - x) * (sx - x) + (2 * n - y - sy) * (2 * n - y - sy);
    if (x == sx && y > sy) {
        three = maxv;
    }

    int min_val = one;
    if (two < min_val) min_val = two;
    if (three < min_val) min_val = three;
    if (four < min_val) min_val = four;

    return min_val;
}

void solution(int m, int n, int startX, int startY, int balls[][2], int ball_count, int answer[]) {
    for (int i = 0; i < ball_count; i++) {
        int x = balls[i][0];
        int y = balls[i][1];
        answer[i] = convert(x, y, startX, startY, m, n);
    }
}
