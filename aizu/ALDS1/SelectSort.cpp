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
    int minj = 0;
    
    for (int i = 0; i < num; i++) {
        minj = i;
        for (int j = i; j < num; j++) {
            if (array[j] < array[minj]) {
                minj = j;
            }
        }
        
        if (i != minj) cnt++;

        tmp = array[i];
        array[i] = array[minj];
        array[minj] = tmp;
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