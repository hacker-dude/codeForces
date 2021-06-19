input()
games = input()
if games.count('A') > games.count('D'):
    print("Anton")
elif games.count('D') > games.count('A'):
    print("Danik")
else:
    print("Friendship")
