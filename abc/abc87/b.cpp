#include <iostream>
#include <string>
using namespace std;

int main()
{
    int a, b, c, x;
    cin >> a >> b >> c >> x;

    int ans = 0;

    for (size_t i = 0; i < a + 1; i++)
    {
        int cur = 500 * i;
        if (cur > x)
        {
            continue;
        }

        for (size_t j = 0; j < b + 1; j++)
        {
            int add = 100 * j;
            int cur2 = cur + add;
            for (size_t k = 0; k < c + 1; k++)
            {
                int add2 = 50 * k;
                if (cur2 + add2 == x)
                {
                    ans += 1;
                }
            }
        }
    }
    cout << ans << endl;
}
