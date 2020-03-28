import sys
import math
from collections import Counter

h, w, k = [int(s) for s in sys.stdin.readline().strip().split()]
s = [''] * h
for i in range(h):
    s[i] = sys.stdin.readline().strip()


ans = float('inf')
for i in range(2 ** h):
    colors = [0]
    cur = 0
    cand = 0
    for div in range(h-1):
        if (i >> div) & 1:
            cur += 1
            colors.append(cur)
            cand += 1
        else:
            colors.append(cur)

    # print('i', i, 'colors', colors)
    impossible = False
    color_count = Counter()
    for j in range(w):
        col_color_count = Counter()
        for row in range(h):
            color = colors[row]
            # print('s', s)
            # print('row', row)
            # print('j', j)
            char = s[row][j]
            if char == '1':
                col_color_count[color] += 1

        has_break = False
        for col in range(cur+1):
            if col_color_count[col] > k:
                impossible = True
                break
            if col_color_count[col] + color_count[col] > k:
                has_break = True
        if impossible:
            break
        if has_break:
            color_count = col_color_count
            cand += 1
        else:
            for col in range(cur+1):
                color_count[col] += col_color_count[col]
    if not impossible:
        ans = min(ans, cand)
print(ans)
