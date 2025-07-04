#include<stdio.h>
#define N 100
#define WHITE 0
#define GRAY 1
#define BLACK 2

int n, M[N][N];
int color[N], d[N], f[N], tt;

void dfs_visit(int u) {
    int v;
    color[u] = GRAY;
    d[u] = ++tt;
    for (int v = 0; v < n; v++) {
        if (M[u][v] == 0) continue;
        if (color[v] == WHITE) {
            dfs_visit(v);
        }
    }
    color[u] = BLACK;
    f[u] = ++tt;
}

void dfs() {
    int u;
    for (int u = 0; u < n; u++) color[u] = WHITE;
    tt = 0;

    for (int u = 0; u < n; u++) {
        if (color[u] == WHITE) dfs_visit(u);
    }
    for (int u = 0; u < n; u++) {
        printf("%d %d %d\n", u + 1, d[u], f[u]);
    }
}

int main() {
    int u, v, k, i, j;

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) M[i][j] = 0;
    }
    
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &u, &k);
        u--;
        for (int j = 0; j < k; j++) {
            scanf("%d", &v);
            v--;
            M[u][v] = 1;
        }
    }

    dfs();
    
    return 0;
}

