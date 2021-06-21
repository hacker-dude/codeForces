a = input()
b = input()
ans = ''
for i, j in zip(a, b):
    if i != j:
        ans += '1'
    else:
        ans += '0'
print(ans)
