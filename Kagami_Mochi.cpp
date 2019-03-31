#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdbool.h>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main(){
  int n = 0;
  int i = 0;
  int j = 0;
  int cnt = 0;
  int tmp = 0;
  bool flg = true;
  
  cin >> n;
  if(n < 1 || 100 < n){
    return 1;
  }
  int d[n];
  for (i = 0; i < n; i++){
    cin >> d[i];
  }
  for(j = 0; j < n; j++){
    if(d[j] < 1 || 100 < d[j]){
      flg = false;
      break;
    }
  }
  //
  if(flg){
    for (i = 100; 0 < i; i--){
      tmp = 0;
      for(j = 0; j < n; j++){
        if(d[j] == i){
          tmp++;
        }
      }
      if(0 < tmp){
        cnt++;
      }
    }
  } else {
    return 1;
  }
  cout << cnt << endl;
  return 0;
}
