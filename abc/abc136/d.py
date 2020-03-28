import sys


def main():
    S = sys.stdin.readline().strip()
    # S = 'RRLLLLRLRRLL'

    def print_ans_part(start, end):
        wall_left = -1
        result = ['0'] * (end - start)
        for i in range(start, end-1):
            if S[i] == 'R' and S[i+1] == 'L':
                wall_left = i
                break

        d_start_wl = (wall_left - start) % 2
        d_wl_end = (end - wall_left) % 2
        wall_left_from_start = wall_left - start

        if (d_start_wl and d_wl_end) or (d_start_wl == 0 and d_wl_end == 0):
            assert (end - start) % 2 == 0
            wl = (end - start) // 2
            wl1 = (end - start) // 2
        else:
            if d_start_wl:
                wl = (end - start) // 2
                wl1 = (end - start) // 2 + 1
            else:
                wl = (end - start) // 2 + 1
                wl1 = (end - start) // 2
        result[wall_left_from_start] = str(wl)
        result[wall_left_from_start+1] = str(wl1)

        print(' '.join(result), end=' ')

    array = []
    cur_is_l = False
    start = 0
    for i in range(len(S)):
        cur = S[i]
        if cur_is_l and cur == 'R':
            print_ans_part(start, i)
            start = i
            array = []
            cur_is_l = False
        else:
            array.append(cur)
            if cur == 'L':
                cur_is_l = True
            else:
                cur_is_l = False
    print_ans_part(start, len(S))
    print('')


main()
