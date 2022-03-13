#include <stdio.h>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

/*
問題文
シカのAtCoDeerくんは二つの正整数a, bを見つけました。
aと bの積が偶数か奇数か判定してください。

制約
1 ≤ a, b ≤ 10000
a, bは整数
*/
int main(){
  int a = 0;
  int b = 0;
  cin >> a >> b;
  if(a < 1 || 10000 < b){
    return 1;
  }
  // 積が奇数なら Odd と、 偶数なら Even と出力せよ。
  if((a * b) % 2 == 0){
    cout << "Even" << endl;
  } else {
    cout << "Odd" << endl;
  }
  return 0;
}
