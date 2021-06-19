def check_luck(n):
    c = ''.join(list(sorted(set(str(n.count('4') + n.count('7'))))))
    if c in '47':
        return True
    else:
        return False


num = input()
if check_luck(num):
    print("YES")
else:
    print("NO")
