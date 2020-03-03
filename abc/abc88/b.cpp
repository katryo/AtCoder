#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int a[n];

    for (size_t i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    sort(a, a + n, greater<int>());

    int alice = 0;
    int bob = 0;
    int turn = 1;
    for (size_t i = 0; i < n; i++)
    {
        if (turn == 1)
        {
            alice += a[i];
        }
        else
        {
            bob += a[i];
        }
        turn *= -1;
    }

    cout << alice - bob << endl;
}
