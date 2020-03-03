#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s;
    cin >> s;

    cout << s << endl;
    int ans = 0;

    if (s[0] == '1')
        ++ans;
    if (s[1] == '1')
        ++ans;
    if (s[2] == '1')
        ++ans;

    cout << ans << endl;
}