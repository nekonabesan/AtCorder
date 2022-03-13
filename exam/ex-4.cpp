#include <bits/stdc++.h>
using namespace std;

/*
1年は何秒か
2年は何秒か
5年は何秒か
10年は何秒か
を順に一行ずつ表示するプログラムを作って下さい。
うるう秒やうるう年のことは考え無くて良いとします
*/
int main() {
  int seconds_per_one_year = 60 * 60 * 24 * 365;
  int seconds_per_twe_year = seconds_per_one_year * 2;
  int seconds_per_five_year = seconds_per_one_year * 5;
  int seconds_per_ten_year = seconds_per_one_year * 10;

  cout << /* 1年は何秒か */ seconds_per_one_year << endl;
  cout << /* 2年は何秒か */ seconds_per_twe_year << endl;
  cout << /* 5年は何秒か */ seconds_per_five_year << endl;
  cout << /* 10年は何秒か */ seconds_per_ten_year << endl;
  return 0;
}
