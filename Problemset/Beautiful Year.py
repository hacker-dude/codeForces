yearStr = input()
yearLen = len(yearStr)  # I Dunno If The Year Gets Bigger Then 4 Digits
year = int(yearStr) + 1
curr = str(year)
while len(set(curr)) != yearLen:
    year += 1
    curr = str(year)
print(curr)
