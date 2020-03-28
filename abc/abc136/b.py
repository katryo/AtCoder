import sys


def main():
    n = int(sys.stdin.readline().strip())

    def digit(num):
        if num < 10:
            return 1
        return digit(num // 10) + 1

    ans = 0
    for i in range(1, n+1):
        if digit(i) % 2:
            ans += 1
    print(ans)


main()
