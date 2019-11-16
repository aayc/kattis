from heapq import heappop, heappush
import sys
oo = float("inf")
L = sys.stdin.readlines()
P, T = [int(x) for x in L[0].split(" ")]
M = [[[] for j in range(T)] for i in range(T)]

for i in range(1, len(L)):
    a, b, d = [int(x) for x in L[i].split(" ")]
    M[a][b].append(d)
    M[b][a].append(d)

D = [oo for i in range(P)]
parents = [[] for i in range(P)]
D[0] = 0
parents[0] = [0]
q = [(0, 0)]
while q:
    dist, node = heappop(q)
    print(node)

    for to_list in range(len(M[node])):
        for to in range(len(M[node][to_list])):
            if dist + M[node][to_list][to] < D[to_list]:
                D[to_list] = M[node][to_list][to] + dist
                parents[to_list].append(node)
                heappush(q, (D[to_list], to))
            elif dist + M[node][to_list][to] == D[to_list]:
                parents[to_list].append(node)

s = [P - 1]
visited = [False for i in range(P)]
visited[P - 1] = True
total = 0
print(parents)
while s:
    node = s.pop()
    for to in parents[node]:
        if len(M[node][to]) == 0:
            continue

        if not visited[to]:
            s.append(to)
                
        visited[to] = True
        min_edge = min(M[node][to])
        for t in M[node][to]:
            if t == min_edge:
                total += min_edge
print(total * 2)


