import sys


def main():
    n = int(sys.stdin.readline().strip())
    d = [int(s) for s in sys.stdin.readline().strip().split()]

    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            ans += d[i] * d[j]
    print(ans)



main()
