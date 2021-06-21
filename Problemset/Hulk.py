hate = 'I hate'
love = 'I love'
that = ' that '
n = int(input())
feelings = ''
for i in range(n):
    if not i & 1:
        feelings += hate
        if i != n - 1:
            feelings += that
    else:
        feelings += love
        if i != n - 1:
            feelings += that
feelings += ' it'
print(feelings)
