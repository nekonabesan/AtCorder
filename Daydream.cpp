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
  string dreamerase("dreamerase");
  string eraseerase("eraseerase");
  string tmp = "\0";
  int i = 0;
  int j = 0;
  int k = 0;
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
  // tを初期化する処理
  for(i = 0; i < cnt; i++){
    t[i] = 0x30;
  }
  //
  for(i = 0; i < cnt; i++){
    for(j = 0; j < 4; j++){
      switch(j){
        case 0:
          tmp = dream;
          break;
        case 1:
          tmp = eraser;
          break;
        case 2:
          tmp = dreamerase;
          break;
        case 3:
          tmp = eraseerase;
          break;
        default:
          tmp = "\0";
          break;
      }
      for(k = 0; k < tmp.size(); k++){
        if(s[i + k] == tmp[k]){
          t[i + k] = tmp[k];
          printf("%c\n",t[i + k]);
        }
      }
    }

    if(s.size() <= t.size()){
      break;
    }
  }

  if(s.size() != t.size()){
    flg = false;
  }

  for(i = 0; i < t.size(); i++){
    if(s[i] != t[i]){
      flg = false;
      break;
    }
  }

  if(flg){
    cout << "YES" << endl;
  } else {
    cout << "NO" << endl;
  }
  return 0;
}
