#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdbool.h>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

/*
*/
int main(){
  int n = 0;
  int i = 0;
  int t = 0;
  int x = 0;
  int y = 0;
  bool flg = true;
  bool flg2 = true;
  //
  cin >> n;
  if(n < 1 || (int)pow(10.0, 5.0) < n){
    return 1;
  }
  //
  int ary_t[n + 1];
  int ary_x[n + 1];
  int ary_y[n + 1];
  ary_t[0] = 0;
  ary_x[0] = 0;
  ary_y[0] = 0;
  for(i = 1; i <= n; i++){
    cin >> t >> x >> y;
    if(t < 1 || (int)pow(10.0, 5.0) < t){
      printf("%d\n", t);
      flg2 = false;
      break;
    }
    if(x < 0 || (int)pow(10.0, 5.0) < x){
      flg2 = false;
      break;
    }
    if(y < 0 || (int)pow(10.0, 5.0) < y){
      flg2 = false;
      break;
    }
    ary_t[i] = t;
    ary_x[i] = x;
    ary_y[i] = y;
    // check t
    if(1 < i && i <= n){
      if(ary_t[i] < ary_t[i - 1]){
        flg2 = false;
        break;
      }
    }
    // check x, y
    if((abs(ary_x[i] - ary_x[i - 1]) + abs(ary_y[i] - ary_y[i - 1])) == 0){
      if((abs(ary_t[i] - ary_t[i - 1]) % 2) != 0){
      	flg = false;
      	break;
      }
    } else {
      if((abs(ary_t[i] - ary_t[i - 1]) < ((abs(ary_x[i] - ary_x[i - 1]) + abs(ary_y[i] - ary_y[i - 1]))))
        ||
        (abs(ary_t[i] - ary_t[i - 1]) % ((abs(ary_x[i] - ary_x[i - 1]) + abs(ary_y[i] - ary_y[i - 1]))) != 0)){
        flg = false;
        break;
      }
    }
  }
  if(flg2 == false){
    return 1;
  } else {
    if(flg == true){
      cout << "YES" << endl;
    } else {
      cout << "NO" << endl;
    }
  }
  return 0;
}
