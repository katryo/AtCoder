#include <iostream>
#include <bits/stdc++.h>
#include <cmath>
#include <vector>

using namespace std;

int main()
{
  int n;
  cin >> n;
  int b[n];
  for (size_t i = 0; i < n - 1; i++)
  {
    cin >> b[i];
  }

  long ans = b[0];

  for (size_t i = 0; i < n - 1; i++)
  {
    ans += b[i];
  }
  cout << ans << endl;
}