import sys
import math
from collections import Counter

n = int(sys.stdin.readline().strip())
a = [int(s) for s in sys.stdin.readline().strip().split()]
c = Counter(a)

total = 0
for key, val in c.items():
    total += val * (val-1) // 2

for i in range(n):
    ai = a[i]
    ai_count = c[ai]

    original = ai_count * (ai_count-1) // 2
    updated = (ai_count-1) * (ai_count-2) // 2
    print(total - original + updated)
