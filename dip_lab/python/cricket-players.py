x = {}

print("How many players?", end=' ')
n = int(input())

for i in range(n):
    print("Enter player name:", end=' ')
    k = input()
    print("Enter runs:", end=' ')
    v = int(input())
    x.update({k: v})

print("\nPlayers in this match:")
for pname in x.keys():
    print(pname)

print("Enter player name:")
name = input()
runs = x.get(name, -1)

if runs == -1:
    print("Player not found")
else:
    print('{} made {} runs.'.format(name, runs))

