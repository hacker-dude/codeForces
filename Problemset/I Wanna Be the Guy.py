n = int(input())
x = set(map(int, input().split()))
y = set(map(int, input().split()))
x.update(y)
try:
    x.remove(0)
except KeyError:
    pass
if len(x) == n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
# incomplete
