n = int(input())
magnets = ""

for i in range(n):
    magnets += input()

print(magnets.count('00') + magnets.count('11') + 1)
