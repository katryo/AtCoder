#include <iostream>
#include <string>
using namespace std;

int sumOfDigits(int n)
{
    int sum = 0;
    while (n > 0)
    {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int main()
{
    int n, a, b;
    cin >> n >> a >> b;

    int ans = 0;
    for (size_t i = 1; i < n + 1; i++)
    {
        int sum = sumOfDigits(i);
        if (a <= sum && sum <= b)
        {
            ans += i;
        }
    }
    cout << ans << endl;
}
