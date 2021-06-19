n = int(input())
m = 0
curr = 0
for i in range(n):
    ex, en = map(int, input().split())
    curr = curr + en - ex
    if curr > m:
        m = curr
print(m)
