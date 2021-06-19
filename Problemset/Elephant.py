n = int(input())
c = 0
for i in range(1, 6)[::-1]:
    if n == n % i:
        continue
    else:
        c += n // i
        n %= i
print(c)

