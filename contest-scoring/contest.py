import sys
L = sys.stdin.readlines()
L = L[:-1]

ps = {}
for i in range(len(L)):
    t, p, result = L[i].strip().split(" ")
    t = int(t)
    solved = result == "right"
    if p not in ps:
        ps[p] = (t, 0 if solved else 1, True if solved else False)
    else:
        ps[p] = (t, ps[p][1] if solved else ps[p][1] + 1, True if solved else False)

n = 0
T = 0
for k, v in ps.items():
    if v[2]:
        T += v[0] + 20 * v[1]
        n += 1
print(n, T)
        
