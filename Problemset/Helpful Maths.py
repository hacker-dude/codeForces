badSum = input().split('+')
print(''.join([f + "+" for f in sorted(badSum)])[:-1], sep="")
