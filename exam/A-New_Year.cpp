#include <iostream>
#include <bits/stdc++.h>
using namespace std;

/*
問題文
12月30日のM時から次の年になるまでは何時間か、求めてください。

制約
1≦M≦23
入力は全て整数
*/
int main() {
  int m = 0;
  int hours = 0;

  cin >> m;
  if(m < 1 || 23 < m){
    return 1;
  }
  hours = 24 - m + 24;
  cout << hours << endl;
  return 0;
}
