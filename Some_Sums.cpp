#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdbool.h>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main(){
  int n = 0;
  int a = 0;
  int b = 0;
  int i = 0;
  int cnt = 0;
  int tmp = 0;
  int line = 0;
  cin >> n >> a >> b;
  if(n < 1 || (int)pow(10.0, 4.0) < n){
    return 1;
  }
  if(a < 1 || 36 < a || b < 1 || 36 < b){
    return 1;
  }
  for(i = 0; i <= n; i++){
    tmp = i;
    line = 0;
    if(0 < tmp / (int)pow(10.0, 4.0)){
      line += tmp / (int)pow(10.0, 4.0);
      tmp = tmp % (int)pow(10.0, 4.0);
    }
    if(0 < tmp / (int)pow(10.0, 3.0)){
      line += tmp / (int)pow(10.0, 3.0);
      tmp = tmp % (int)pow(10.0, 3.0);
    }
    if(0 < tmp / (int)pow(10.0, 2.0)){
      line += tmp / (int)pow(10.0, 2.0);
      tmp = tmp % (int)pow(10.0, 2.0);
    }
    if(0 < tmp / 10){
      line += tmp/10;
      tmp = tmp % 10;
    }
    line += tmp;
    if(a <= line && line <= b){
      cnt+=i;
    }
  }
  cout << cnt << endl;
  return 0;
}
