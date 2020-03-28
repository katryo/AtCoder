import sys
from collections import deque
from heapq import heappush, heappop

def main():
    n_d_a = sys.stdin.readline().strip().split(' ')
    n, d, a = [int(s) for s in n_d_a]
    # n = 5
    # d = 1
    # a = 3
    # xh = [[0, 7],[1, 9], [2, 10], [4, 15], [20, 8]]

    xh = [[]] * n

    for i in range(n):
        x, h = [int(s) for s in sys.stdin.readline().strip().split(' ')]
        xh[i] = [x, h]
    xh.sort()

    cur = 0
    attack_rightmost_idx = [-1] * n
    for i in range(n):
        x, h = xh[i]
        attack_rightmost = x + 2 * d
        while cur < n-1 and xh[cur+1][0] <= attack_rightmost:
            cur += 1
        attack_rightmost_idx[i] = cur

    events = deque()
    total_damage = 0
    ans = 0
    for i in range(n):
        while events and events[0][0] <= i:
            total_damage += events[0][1]
            events.popleft()

        x, h = xh[i]

        remaining_life = h - total_damage
        if remaining_life <= 0:
            continue

        needed = remaining_life // a
        if remaining_life % a:
            needed += 1
        ans += needed
        total_damage += needed * a
        events.append((attack_rightmost_idx[i]+1, - needed * a))

    print(ans)


if __name__ == '__main__':
    main()
