#include<iostream>
#include<algorithm>
#define MAX 100000
using namespace std;

int n;
int A[MAX+1];
int L[MAX];

int lis()
{
    L[0] = A[0];
    int length = 1;

    for (int i = 1; i < n; i++) {
        if (L[length - 1] < A[i]) {
            L[length++] = A[i];
        } else {
            *lower_bound(L, L + length, A[i]) = A[i];
        }
    }

    return length;
}

int main()
{
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    cout << lis() << endl;

    return 0;
}



