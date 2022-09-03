#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;
using std::vector;

void echo(int array[], int num) {
    for(int i = 0; i < num; i++) {
        if(i > 0) cout << " ";
        cout << array[i];
    }
    cout << endl;
}

void insertSort(int array[], int num, int g, long long &cnt) {
    int tmp;
    int j;

    for (int i = g; i < num; i++) {
        tmp = array[i];
        j = i - g;
        while (j >= 0 && array[j] > tmp) {
            array[j + g] = array[j];
            j -= g;
            cnt++;
        }
        array[j + g] = tmp;
        //echo(array, num);
    }
}

vector<int> shellSort(int array[], int num, long long &cnt) {
    vector<int> arrayG;

    for (int h = 1; ; ) {
        if (h > num) {
            break;
        }
        arrayG.push_back(h);
        h = 3 * h + 1;
    }

    for (int i = arrayG.size(); i >= 0 ; i--) {
        insertSort(array, num, arrayG[i], cnt);
    }

    return arrayG;
}

int main(void) {
    int num = 0;
    int size = 0;
    long long cnt = 0;
    vector<int> arrayG;
    
    cin >> num;

    int *array = (int *)malloc(num * sizeof(int));

    for (int i = 0; i < num; i++) {
        scanf("%d", &array[i]);
    }

    arrayG = shellSort(array, num, cnt);

    cout << arrayG.size() << endl;
    for (int i = arrayG.size() - 1; i >= 0; i--) {
        printf("%d", arrayG[i]);
        if(i) printf(" ");
    }
    printf("\n");
    printf("%lld\n", cnt);
    for (int i = 0; i < num; i++) {
        printf("%d\n", array[i]);
    }

    free(array);

    return 0;
}

