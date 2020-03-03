#include <iostream>
#include <string>
using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;

    int mul = a * b;
    if (mul % 2 == 1)
    {
        cout << "Odd" << endl;
    }
    else
    {
        cout << "Even" << endl;
    }
}