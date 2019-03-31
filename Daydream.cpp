#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdbool.h>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main(){
  string s;
  string t;
  string dream("dream");
  string dreamer("dreamer");
  string erase("erase");
  string eraser("eraser");
  string tmp;
  int i = 0;
  int j = 0;
  int pos = 0;
  int cnt = 0;
  bool flg = true;
  cin >> s;
  cnt = s.size();
  for(i = 0; i < s.size(); i++){
    if(s[i] < 97 || 122 < s[i]){
      flg = false;
      break;
    }
  }
  if(cnt < 1 || (int)pow(10.0, 5.0) < cnt || flg == false){
    return 1;
  }

  while(true){
    
  }

  if(flg){
    cout << "YES" << endl;
  } else {
    cout << "NO" << endl;
  }
  return 0;
}
