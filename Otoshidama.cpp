#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdbool.h>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main(){
  int n = 0;
  int yen = 0;
  int i = 0;
  int j = 0;
  int k = 0;
  int x = 0; // 10000
  int y = 0; // 5000
  int z = 0; // 1000
  int tmp = 0;
  int cnt = 0;
  bool flg = false;
  cin >> n >> yen;
  if(n < 1 || 2000 < n){
    return 1;
  }
  if(yen < 1000 || (2 * (int)pow(10.0, 7.0)) < yen){
    return 1;
  }
  if(yen % 1000 != 0){
    return 1;
  } else {
    yen = yen / 1000;
  }

  for(i = 0; i <= n; i++){
    // 1000
    for(j = 0; j <= (n - i); j++){
      // 5000
      for(k = 0; k <= (n - i - j); k++){
        // 10000
        if((1 * i) + (5 * j) + (10 * k) == yen && (i + j + k) == n && tmp == 0){
          x = k;
          y = j;
          z = i;
          flg = true;
          break;
        }
      }
      if(flg == true){
        break;
      }
    }
    if(flg == true){
      break;
    }
  }

  if(flg){
    cout << x << " " << y << " " << z << endl;
  } else {
    cout << "-1 -1 -1" << endl;
  }
  return 0;
}
