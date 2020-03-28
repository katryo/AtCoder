import sys

n, p = [int(s) for s in sys.stdin.readline().strip().split()]
s = sys.stdin.readline().strip()

dic = [0] * p
ans = 0

for i in range(n):
    num = int(s[i])
    for key, val in enumerate(dic):
        if val > 0:
            rem = (key * 10 + num) % p
            dic[rem] += val
            dic[key] -= val
    dic[num % p] += 1
    ans += dic[0]

print(ans)
