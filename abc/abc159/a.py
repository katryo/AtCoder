import sys
import math

n, m = [int(s) for s in sys.stdin.readline().strip().split()]

print(m * (m-1) // 2 + n * (n-1) // 2)
