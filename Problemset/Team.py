from datetime import datetime
a = datetime.now()
n = int(input())
c = 0
for i in range(n):
    if input().count('1') >= 2:
        c += 1
print(c)
print(datetime.now() - a)
