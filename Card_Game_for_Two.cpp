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
  int k = 0;
  int tmp = 0;
  int alice = 0;
  int bob = 0;
  int max = 0;
  string s;
  bool flg = true;
  cin >> n;
  if(n < 1 || 100 < n){
    return 1;
  }
  int a[n];
  while(getline(cin, s, ' ')) {
    a[i] = stoi(s);
    i++;
  }
  for (j = 0; j < n; j++){
    if(a[j] < 1 || 100 < a[j]){
      flg = false;
      break;
    }
  }
  if(flg){
    for (j = 1; j <= n; j++){
      max = 0;
      for(int k = 0; k < n; k++){
        if(max < a[k]){
          max = a[k];
          tmp = k;
        }
      }
      if(j % 2 == 0){
        bob += max;
        a[tmp] = -1;
      } else {
        alice += max;
        a[tmp] = -1;
      }
    }
  } else {
    return 1;
  }
  cout << alice - bob << endl;
  return 0;
}
