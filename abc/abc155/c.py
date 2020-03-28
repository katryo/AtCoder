import sys
from collections import Counter

n = int(sys.stdin.readline().strip())

ss = []
counter = Counter()
for i in range(n):
    s = sys.stdin.readline().strip()
    counter[s] += 1
    ss.append(s)

count_items = counter.most_common()
count_max = count_items[0][1]
ans = []


for count_item in count_items:
    if count_max == count_item[1]:
        ans.append(count_item[0])
    else:
        break

ans.sort()
for word in ans:
    print(word)
