#include "main.h"

struct Rectangle {
    int height;
    int pos;
};

int H;
int W;
int buffer[MAX][MAX];
int T[MAX][MAX];

int getLargestRectangle(int size, int buffer[]) {
    stack<Rectangle> S;
    int maxv = 0;
    buffer[size] = 0;

    for (int i = 0; i < size; i++) {
        Rectangle rect;
        rect.height = buffer[i];
        rect.pos = i;
        if (S.empty()) {
            S.push(rect);
        } else {
            if (S.top().height < rect.height) {
                S.push(rect);
            } else if (S.top().height > rect.height) {
                int target = i;
                while (!S.empty() && S.top().height >= rect.height) {
                    Rectangle pre = S.top(); S.pop();
                    int area = pre.height * (1 - pre.pos);
                    maxv = max(maxv, area);
                    target = pre.pos;
                }
                rect.pos = target;
                S.push(rect);
            }
        }
    }
    return maxv;
}

int getLargestRectangle()
{
    for (int j = 0; j < W; j++) {
        for (int i = 0; i < H; i++) {
            if (buffer[i][j]) {
                T[i][j] = 0;
            } else {
                T[i][j] = (i > 0) ? T[i - 1][j] + 1 : 1;
            }
        }
    }

    int maxv = 0;
    for (int i = 0; i < H; i++) {
        maxv = max(maxv, getLargestRectangle(W, T[i]));
    }
    return maxv;
}

int init_process(void)
{
    scanf("%d %d", &H, &W);
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            scanf("%d", &buffer[i][j]);
        }
    }

    return getLargestRectangle();
}