N, P, M = [int(x) for x in input().split(" ")]
names = { m: 0 for m in [input() for i in range(N)] }
won = False
winners = set([])
for i in range(M):
    name, pts = input().split(" ")
    names[name] += int(pts)
    if names[name] >= P and name not in winners:
        winners.add(name)
        print(name, "wins!")
        won = True

if not won:
    print("No winner!")
