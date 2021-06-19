word = input()
uc = lc = 0
for i in word:
    if i.islower():
        lc += 1
    else:
        uc += 1
if lc > uc:
    print(word.lower())
elif uc > lc:
    print(word.upper())
else:
    print(word.lower())
