#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

void echo(int array[], int num) {
    for(int i = 0; i < num; i++) {
        if(i > 0) printf(" ");
        printf("%d", array[i]);
    }
    printf("\n");
}

int sort(int array[], int num) {
    int tmp = 0;
    int cnt = 0;
    int flg = 1;
    int j;

    
    while (flg == 1) {
        flg = 0;
        for (int i = num - 1; i >= 1; i--) {
            if (array[i] < array[i - 1]) {
                tmp = array[i];
                array[i] = array[i - 1];
                array[i - 1] = tmp;
                flg = 1;
                cnt++;
            }
        }
    }

    return cnt;
}

int main(void) {
    int num = 0;
    int cnt = 0;
    
    scanf("%d", &num);

    int *array = (int *)malloc(num * sizeof(int));

    for (int i = 0; i < num; i++) {
        scanf("%d", &array[i]);
    }

    cnt = sort(array, num);
    
    echo(array, num);
    printf("%d\n", cnt);
    
    free(array);

    return 0;
}