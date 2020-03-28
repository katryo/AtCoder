import sys

a = [[0] * 3 for _ in range(3)]
a[0] = list(map(int, sys.stdin.readline().strip().split()))
a[1] = list(map(int, sys.stdin.readline().strip().split()))
a[2] = list(map(int, sys.stdin.readline().strip().split()))
n = int(sys.stdin.readline().strip())
b = [0] * n
for i in range(n):
    b = int(sys.stdin.readline().strip())

    for row in range(3):
        for col in range(3):
            if a[row][col] == b:
                a[row][col] = 0


def is_bingo():
    # horizontal
    for r in range(3):
        if a[r][0] + a[r][1] + a[r][2] == 0:
            return True
    # vertical
    for c in range(3):
        if a[0][c] + a[1][c] + a[2][c] == 0:
            return True

    if a[0][0] + a[1][1] + a[2][2] == 0:
        return True
    if a[2][0] + a[1][1] + a[0][2] == 0:
        return True

    return False


if is_bingo():
    print('Yes')
else:
    print('No')


