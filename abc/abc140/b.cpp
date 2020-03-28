#include <iostream>
#include <bits/stdc++.h>
#include <cmath>
#include <vector>

using namespace std;

int main()
{
  int n;
  cin >> n;
  // n = 3;
  vector<int> a;
  vector<int> b;
  vector<int> c;

  a.assign(n, 0);
  b.assign(n, 0);
  c.assign(n, 0);

  for (size_t i = 0; i < n; i++)
  {
    cin >> a[i];
  }

  for (size_t i = 0; i < n; i++)
  {
    cin >> b[i];
  }

  for (size_t i = 0; i < n - 1; i++)
  {
    cin >> c[i];
  }

  int total = 0;
  int bonus_num = 0;

  for (size_t i = 0; i < n; i++)
  {
    int num = a[i];
    int score = b[num - 1];
    total += score;
    if (bonus_num == num)
    {
      total += c[num - 2];
    }
    bonus_num = num + 1;
  }
  cout << total << endl;
}