import sys


def main():
    s = sys.stdin.readline().strip()

    n = len(s)
    # n: 3, half: 2
    # n: 4, half: 2
    # n: 5, half: 3
    half = n // 2 + (n % 2)

    ans = 0
    for i in range(half):
        if s[i] != s[-1-i]:
            ans += 1
    print(ans)


main()
