#include <stdio.h>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

/*
問題文
2つの正整数 a, bが与えられます。
a, bの平均値を xとします。 xの小数点以下を切り上げて得られる整数を出力してください。

制約
a, bは整数である。
 1≤a, b≤100
*/
int main(){
  int a = 0;
  int b = 0;
  double x = 0.0;
  scanf("%d", &a);
  scanf("%d", &b);
  if(a < 1 || 100 < b){
    return 1;
  }
  x = ((double)a + (double)b) / 2.0;
  if((x - (int)x) == 0.0){
    cout << (int)x << endl;
  } else {
    cout << (int)x + 1 << endl;
  }
  return 0;
}
