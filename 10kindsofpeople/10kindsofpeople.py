from collections import deque
import sys


def dfs(r, c, i, prev):
    if 0 <= r < len(M) and 0 <= c < len(M[0]) \
            and M[r][c] == prev and V[r][c] is None:
        V[r][c] = i
        dfs(r + 1, c, i, prev)
        dfs(r, c + 1, i, prev)
        dfs(r - 1, c, i, prev)
        dfs(r, c - 1, i, prev)

L = sys.stdin.readlines()
R, C = [int(x) for x in L[0].split(" ")]
M = [list(i.strip()) for i in L[1:R + 1]]
V = [[None for j in range(C)] for i in range(R)]
#print(len(M), len(M[0]),  len(V), len(V[0]))

i = 0
for r in range(len(M)):
    for c in range(len(M[r])):
        if V[r][c] is None:
            dfs(r, c, i, M[r][c])
            i += 1
#for v in V:
#    print(*v)
T = int(L[R + 1])
L = L[R + 2:]

for t in range(T):
    a, b, c, d = [int(x) - 1 for x in L[t].strip().split(" ")]
    user = "decimal" if M[a][b] == '1' else "binary"
    if V[a][b] == V[c][d]:
        print(user)
    else:
        print("neither")
