#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdbool.h>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main(){
  int i = 0;
  int j = 0;
  int n = 0;
  string s;
  int max = (int)pow(10.0, 9.0);
  int cnt = 0;
  int flg = true;
  cin >> n;
  int a[n];
  while(getline(cin, s, ' ')) {
    a[i] = stoi(s);
    i++;
  }
  if(n < 1 || 200 < n){
    flg = false;
  }
  for (j = 0; j < n; j++){
    if(max < a[j]){
      flg = false;
    }
  }
  while(flg){
    for(j = 0; j < n; j++){
      if(a[j] % 2 != 0){
        flg = false;
      }
      a[j] = a[j] / 2;
      if(a[j] < 1){
        flg = false;
      }
    }
    if(flg){
      cnt++;
    }
  }
  cout << cnt << "\n";
  return 0;
}
