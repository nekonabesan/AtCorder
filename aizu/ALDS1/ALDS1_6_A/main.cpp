#include<stdio.h>
#include<stdlib.h>
#define MAX 2000001
#define VMAX 10000

int main()
{
    unsigned short *A, *B;
    int C[VMAX + 1];
    int n, i, j;
    scanf("%d", &n);

    A = (unsigned short *)malloc(n * sizeof(short) + 1);
    B = (unsigned short *)malloc(n * sizeof(short) + 1);

    for (int i = 0; i < n; i++) C[i] = 0;

    for (i = 0; i < n; i++) {
        scanf("%hu", &A[i + 1]);
        C[A[i + 1]]++;
    }

    for (i = 1; i <= VMAX; i++) C[i] = C[i] + C[i - 1];

    for (j = 1; j <= n; j++) {
        B[C[A[j]]] = A[j];
        C[A[j]]--;
    }

    for (i = 1; i <= n; i++) {
        if (i > 1) printf(" ");
        printf("%hu", B[i]);
    }

    printf("\n");

    return 0;
}