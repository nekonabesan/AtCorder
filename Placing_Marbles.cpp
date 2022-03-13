#include <stdio.h>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

/*
問題文
すぬけ君は 1, 2, 3の番号がついた 3つのマスからなるマス目を持っています。
各マスには 0 か 1 が書かれており、マス iには s_iが書かれています。

すぬけ君は 1 が書かれたマスにビー玉を置きます。
ビー玉が置かれるマスがいくつあるか求めてください。

制約
s1, s2, s3は 1 あるいは 0
*/
int main(){
  string a;
  int s1 = 0;
  int s2 = 0;
  int s3 = 0;
  cin >> a;
  if(std::stoi(a) & 0x04){
    s1 = 1;
  }
  if(std::stoi(a) & 0x02){
    s2 = 1;
  }
  if(std::stoi(a) & 0x01){
    s3 = 1;
  }
  if(s1 != 0 || s1 != 1 || s2 != 0 || s2 != 1 || s3 != 0 || s3 != 1){
    //return 1;
  }
  cout << s1 + s2 + s3 << endl;
  return 0;
}
