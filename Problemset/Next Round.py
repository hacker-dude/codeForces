n, k = list(map(int, input().split()))
contestants = list(map(int, input().split()))
kScore = contestants[k-1]
c = 0
for i in contestants:
    if i >= kScore and i != 0:
        c += 1
print(c)
