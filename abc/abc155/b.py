import sys

n = int(sys.stdin.readline().strip())
a = [int(s) for s in sys.stdin.readline().strip().split(' ')]

app = True
for ai in a:
    if ai % 2 == 0:
        if ai % 3 != 0 and ai % 5 != 0:
            app = False

if app:
    print('APPROVED')
else:
    print('DENIED')
