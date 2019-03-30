#include <stdio.h>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

/*
問題文
高橋君はあるプログラミングコンテストが行われているサイトに参加しています。
ここでは, コンテストに出場した時にこの順位に応じて「パフォーマンス」というものがつき、
それによってレーティング (整数とは限らない) が次のように変化します。

現在のレーティングを aとする。
 次のコンテストで, パフォーマンス bを取ったとする。
そのとき, レーティングは aと bの平均まで変化する。
 例えば, レーティングが 1の人が次のコンテストでパフォーマンス 1000を取ったら,
レーティングは 1と 1000の平均である 500.5になります。
高橋君は, 現在のレーティングが Rで, 次のコンテストでレーティングをちょうど Gにしたいと思っています。
 そのとき, 高橋君が取るべきパフォーマンスを求めなさい。

制約
0≤R
G≤4500
入力はすべて整数
*/
int main(){
  int r;
  int g;
  double x = 0.0;
  scanf("%d", &r);
  scanf("%d", &g);
  if(r < 0 || 4500 < g){
    return 1;
  }
  x = (2 * g) - r;
  cout << x << endl;
  return 0;
}
