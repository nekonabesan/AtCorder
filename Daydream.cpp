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

  while(flg){
    flg = false;
    // dreamerase
    if(s.substr(pos, pos + (dreamerase.size() -1)) == dreamerase){
      t += dreamerase;
      pos += (dreamerase.size() -1);
      flg = true;
    }
    // eraseerase
    if(s.substr(pos, pos + (eraseerase.size() -1)) == eraseerase){
      t += eraseerase;
      pos += (eraseerase.size() -1);
      flg = true;
    }
    // dreamer
    if(s.substr(pos, pos + (dreamer.size() -1)) == dreamer){
      t += dreamer;
      pos += (dreamer.size() -1);
      flg = true;
    }
    // eraser
    if(s.substr(pos, pos + (eraser.size() -1)) == eraser){
      t += eraser;
      pos += (eraser.size() -1);
      flg = true;
    }
    // dream
    if(s.substr(pos, pos + (dream.size() -1)) == dream){
      t += dream;
      pos += (dream.size() -1);
      flg = true;
    }
    // erase
    if(s.substr(pos, pos + (erase.size() -1)) == erase){
      t += erase;
      pos += (erase.size() -1);
      flg = true;
    }
    if(s.size() <= t.size()){
      break;
    }
  }

  if(s != t){
    flg = false;
  }

  if(flg){
    cout << "YES" << endl;
  } else {
    cout << "NO" << endl;
  }
  return 0;
}
