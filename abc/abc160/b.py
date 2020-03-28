import sys
import math
from collections import Counter

n = int(sys.stdin.readline().strip())
print(n // 500 * 1000 + (n % 500) // 5 * 5)
