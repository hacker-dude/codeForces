n = int(input())
stones = input()
new = stones
while 'RR' in new:
    new = new.replace('RR', 'R')
while 'GG' in new:
    new = new.replace('GG', 'G')
while 'BB' in new:
    new = new.replace('BB', 'B')
print(n - len(new))

