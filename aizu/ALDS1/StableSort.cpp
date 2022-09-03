#include <iostream>
using namespace std;

struct Card{
    char suit;
    char value;
};

void echo(struct Card array[], int num) {
    for(int i = 0; i < num; i++) {
        if(i > 0) cout << " ";
        cout << array[i].suit << array[i].value;
    }
    cout << endl;
}

int bubbleSort(struct Card array[], int num) {
    struct Card tmp;
    int cnt = 0;
    int flg = 1;
    int j;

    
    while (flg == 1) {
        flg = 0;
        for (int i = num - 1; i >= 1; i--) {
            if (array[i].value < array[i - 1].value) {
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

int sellectSort(struct Card array[], int num) {
    struct Card tmp;
    int cnt = 0;
    int minj = 0;
    
    for (int i = 0; i < num; i++) {
        minj = i;
        for (int j = i; j < num; j++) {
            if (array[j].value < array[minj].value) {
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

bool isStable(struct Card array1[], struct Card array2[], int num) {
    bool ret = true;
    for (int i = 0; i < num; i++) {
        if (array1[i].suit != array2[i].suit) {
            ret = false;
            break;
        }
    }

    return ret;
} 

int main(void) {
    int num = 0;
    int cnt = 0;
    
    cin >> num;

    struct Card *array1 = (Card *)malloc(num * sizeof(Card));
    struct Card *array2 = (Card *)malloc(num * sizeof(Card));

    for (int i = 0; i < num; i++) {
        cin >> array1[i].suit >> array1[i].value;
    }

    for (int i = 0; i < num; i++) {
        array2[i] = array1[i];
    }

    bubbleSort(array1, num);
    sellectSort(array2, num);

    echo(array1, num);
    cout << "Stable" <<endl;
    echo(array2, num);
    if (isStable(array1, array2, num)) {
        cout << "Stable" <<endl;
    } else {
        cout << "Not Stable" <<endl;
    }
    
    free(array1);
    free(array2);

    return 0;
}

