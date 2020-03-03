#include <iostream>
#include <string>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int a[n];

    bool has_odd = false;
    for (size_t i = 0; i < n; i++)
    {
        cin >> a[i];
        if (a[i] % 2 == 1)
        {
            has_odd = true;
        }
    }

    if (has_odd)
    {
        cout << 0 << endl;
        return 0;
    }

    int ans = 0;
    while (true)
    {
        for (size_t i = 0; i < n; i++)
        {
            if (a[i] % 2 == 1)
            {
                cout << ans << endl;
                return 0;
            }
        }
        for (size_t i = 0; i < n; i++)
        {
            a[i] /= 2;
        }

        ans += 1;
    }
}