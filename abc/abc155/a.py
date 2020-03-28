import sys

abc = [int(s) for s in sys.stdin.readline().strip().split(' ')]

a = abc[0]
b = abc[1]
c = abc[2]

is_kawai = False

if a == b:
    if b == c:
        pass
    else:
        is_kawai = True
elif b == c:
    is_kawai = True
elif a == c:
    is_kawai = True

if is_kawai:
    print('Yes')
else:
    print('No')


