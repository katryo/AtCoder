#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
  int N;
  cin >> N;
  vector<long long> L(N);
  for (int i = 0; i < N; ++i)
    cin >> L[i];
  sort(L.begin(), L.end()); // L をソートしておく

  long long res = 0;

  // a を固定して、(b, c) をしゃくとり法
  for (int i = 0; i < N; ++i)
  {
    int k = i;
    for (int j = i + 1; j < N; ++j)
    {
      while (k < N && L[k] < L[i] + L[j])
        ++k;
      res += k - (j + 1);
    }
  }
  cout << res << endl;
}