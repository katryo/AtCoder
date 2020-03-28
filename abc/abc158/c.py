import sys
import math

a, b = [int(s) for s in sys.stdin.readline().strip().split()]

ans = -1
for i in range(1, 2000):
    if math.floor(i * 0.08) == a and math.floor(i * 0.1) == b:
        ans = i
        break
print(ans)
