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

void sort(int array[], int num) {
    int tmp, j;
    for (int i = 1; i < num; i++) {
        tmp = array[i];
        j = i - 1;
        while (j >= 0 && array[j] > tmp) {
            array[j + 1] = array[j];
            j--;
        }
        array[j + 1] = tmp;
        echo(array, num);
    }
}

int main(void) {
    int num = 0;
    
    scanf("%d", &num);

    int *array = (int *)malloc(num * sizeof(int));

    for (int i = 0; i < num; i++) {
        scanf("%d", &array[i]);
    }

    echo(array, num);
    sort(array, num);
    free(array);

    return 0;
}