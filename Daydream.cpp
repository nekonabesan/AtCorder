#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdbool.h>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main(){
  string s;
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
  bool flg = true;
  cin >> s;
  string t(s.size(), 0x30);
  for(i = 0; i < s.size(); i++){
    if(s[i] < 97 || 122 < s[i]){
      flg = false;
      break;
    }
  }
  if(s.size() < 1 || (int)pow(10.0, 5.0) < s.size() || flg == false){
    return 1;
  }
  //
  for(i = 0; i < s.size(); i++){
    for(j = 0; j < 4; j++){
      switch(j){
        case 0:
          tmp = dream;
          break;
        case 1:
          tmp = erase;
          break;
        case 2:
          tmp = dreamer;
          break;
        case 3:
          tmp = eraser;
          break;
        default:
          tmp = "\0";
          break;
      }

      if(!tmp.empty() && (i + tmp.size()) <= s.size()){
        for(k = 0; k < tmp.size(); k++){
          if(s[i + k] == tmp[k]){
            t[i + k] = tmp[k];
          } else {
            break;
          }
        }
      }
    }
  }

  if(s.size() != t.size()){
    flg = false;
  }

  for(i = 0; i < s.size(); i++){
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
