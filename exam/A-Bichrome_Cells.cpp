#include <stdio.h>
#include <math.h>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

/*
問題文N × Nのマス目があります。
このマス目の各マスを白色または黒色に塗ることにしました (すべてのマスをどちらか片方の色に塗ります)。
ちょうど Aマスを白色に塗るとき、黒色に塗ることになるマスはいくつあるでしょうか。

制約
1≦N≦100
0≦A≦N^2
*/
int main(){
  int n = 0;
  int a = 0;
  double cells = 0.0;
  scanf("%d", &n);
  scanf("%d", &a);
  cells = pow(n, 2.0);
  if(n < 0 || 100 < n || a < 0 || cells < (double)a){
    return 1;
  }
  cout << (int)cells - a << endl;
  return 0;
}
