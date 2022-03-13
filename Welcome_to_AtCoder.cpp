#include <stdio.h>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

/*
問題文
高橋君はデータの加工が行いたいです。
整数 a,b,cと、文字列 s が与えられます。
整数 a+b+c と、文字列 s を並べて表示しなさい。
*/
int main(){
  int a = 0;
  int b = 0;
  int c = 0;
  string s;
  cin >> a;
  cin >> b >> c;
  cin >> s;
  cout << (a + b + c) << " " << s << endl;
  return 0;
}
