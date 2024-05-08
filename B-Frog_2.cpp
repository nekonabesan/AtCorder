#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;

const long long INF = 1LL << 60;
const long long ARRAY_LENGTH = 100010;

long long height[ARRAY_LENGTH];
long long dp[ARRAY_LENGTH];

long long get_min(long long num1, long long num2)
{
  if (num1 >= num2) {
    return num2;
  }
  return num1;
}

int main()
{
  int NUM = 0;
  int HOP = 0;
  cin >> NUM;
  cin >> HOP;
  
  for (int i = 0; i < NUM; ++i) cin >> height[i];

  for (int i = 0; i < ARRAY_LENGTH; ++i) dp[i] = INF;
   
  dp[0] = 0; 
  for (int i = 0; i < NUM; i++)
  {
    for (int j = 1; j <= HOP; j++)
    {
      dp[i + j] = get_min(dp[i + j], dp[i] + abs(height[i] - height[i + j]));
    }
  }
  cout << dp[NUM - 1] << endl;
}