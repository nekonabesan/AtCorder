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
  cin >> NUM;
  for (int i = 0; i < NUM; ++i) cin >> height[i];

  for (int i = 0; i < ARRAY_LENGTH; ++i) dp[i] = INF;
    
  for (int i = 0; i < NUM; i++)
  {
    if (i == 0) {
      dp[i] = 0;
      continue;
    } else if (i == 1) {
      dp[i] = dp[i - 1] + abs(height[i] - height[i - 1]);
      continue;
    }
    dp[i] = get_min(dp[i - 1] + abs(height[i] - height[i - 1]), dp[i - 2] + abs(height[i] - height[i - 2]));
  }
  cout << dp[NUM - 1] << endl;
}