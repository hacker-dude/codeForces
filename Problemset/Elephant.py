n = int(input())
c = 0
for i in range(1, 6)[::-1]:
    if n == n % i:
        continue
    else:
        c += n // i if n % i != 0 else 1
        n //= i
#    print(c, n, i)
print(c)
# incomplete
