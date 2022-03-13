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
  int a = 0; //500
  int b = 0; //100
  int c = 0; //50
  int x = 0;
  int i = 0;
  int j = 0;
  int k = 0;
  int amt = 0;
  int cnt = 0;
  cin >> a;
  cin >> b;
  cin >> c;
  cin >> x;
  if(a < 0 || 50 < a || b < 0 || 50 < b || c < 0 || 50 < c){
    return 1;
  }
  if((a + b + c) < 1){
    return 1;
  }
  if(x < 50 || 20000 < x){
    return 1;
  }
  if(x % 50 != 0){
    return 1;
  }
  // 合計金額未達
  if((500 * a) + (100 * b) + (50 * c) < x){
    cout << 0 << endl;
    return 0;
  }

  //
  for (i = 0; i <= a; i++){
    amt = 0;
    amt += (500 * i);
    if(amt == x){
      amt = 0;
      cnt++;
      break;;
    }
    //
    for (j = 0; j <= b; j++){
      amt += (100 * j);
      if(amt == x){
        amt -= (100 * j);
        cnt++;
        break;
      }
      //
      for (k = 0; k <= c; k++){
        amt += (50 * k);
        if(amt == x){
          amt -= (50 * k);
          cnt++;
          break;
        }
        amt -= (50 * k);
      }
      amt -= (100 * j);
    }
    amt = 0;
  }
  cout << cnt << endl;
  return 0;
}
