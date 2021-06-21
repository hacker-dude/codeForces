n = int(input())
gifts = list(map(int, input().split()))
gifted = [None] * n

for i, gift in enumerate(gifts):
    gifted[gift - 1] = i + 1

print(*gifted)
