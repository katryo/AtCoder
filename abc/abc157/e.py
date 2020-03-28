import sys
from collections import Counter
from copy import deepcopy

def main():
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    q = int(sys.stdin.readline().strip())

    dp = [0] * n

    counter = Counter
    for i in range(n):
        letter = s[i]
        counter[letter] += 1
        dp[i] = deepcopy(counter)




result = main()
print(result)
