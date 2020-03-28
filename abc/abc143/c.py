import sys


def main():
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()

    cur = '@'
    ans = 0
    for i in range(n):
        if cur != s[i]:
            ans += 1
        cur = s[i]
    print(ans)


main()
