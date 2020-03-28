import sys

s = sys.stdin.readline().strip()
l = len(s)

half = l // 2

left = s[:half]

if half * 2 == l:
    right = s[half:]
else:
    right = s[half+1:]


def is_pal(string):
    return string == string[::-1]


if is_pal(s) and is_pal(left) and is_pal(right):
    print('Yes')
else:
    print('No')
