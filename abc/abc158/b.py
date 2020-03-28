import sys

n, a, b = [int(s) for s in sys.stdin.readline().strip().split(' ')]
ab = a + b
dividend = n // ab

ans = dividend * a + min(n % ab, a)
print(ans)
