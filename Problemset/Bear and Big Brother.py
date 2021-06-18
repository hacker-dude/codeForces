a, b = map(int, input().split())
c = 0
while b >= a:
    a *= 3
    b *= 2
    c += 1
print(c)
