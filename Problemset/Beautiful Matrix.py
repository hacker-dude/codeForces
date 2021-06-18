matrix = []
xOf1 = None
yOf1 = None
for i in range(5):
    row = input().split()
    if '1' in row:
        xOf1 = i
        yOf1 = row.index('1')
    matrix.append(row)
print(abs(2 - xOf1) + abs(2 - yOf1))
