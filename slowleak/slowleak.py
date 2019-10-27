from heapq import heappop, heappush
import sys
L = sys.stdin.readlines()

oo = float("inf")
N, M, T, start_air = [int(x) for x in L[0].split(" ")]
rest_stops = set([int(x) - 1 for x in L[1].split(" ")])


class Node:
    def __init__(self):
        self.neighbors = []
    
    def add_neighbor(self, neighbor, w):
        self.neighbors.append((neighbor, w))

nodes = [Node() for i in range(N)]
L = L[2:]
for i in range(M):
    f, t, d = [int(x) for x in L[i].split(" ")]
    nodes[f - 1].add_neighbor(t - 1, d)
    nodes[t - 1].add_neighbor(f - 1, d)


# Do a weighted BFS, storing statistic
q = [(0, start_air, 0)] # distance, air, node
memo = {0: [(0, start_air)]}
bssf = oo
while q:
    d, air, n = heappop(q)
    node = nodes[n]

    # refill if this is a rest stop
    if n in rest_stops:
        air = start_air

    if n == N - 1:
        bssf = min(bssf, d)
        
        continue
    
    for neighbor, w in node.neighbors:
        if air - w < 0:
            # don't have enough air
            continue

        if neighbor in memo:
            strictly_worse = False
            for saved_distance, saved_air in memo[neighbor]:
                #print("neighbor:", neighbor)
                #print("\tsaved:", saved_distance, saved_air)
                #print("\tthis:", d + w, air - w)
                if saved_distance <= d + w and saved_air >= air - w:
                    strictly_worse = True

            if strictly_worse:
                continue
            else:
                #print("not strictly worse")
                pass
        else:
            memo[neighbor] = []
    
        q.append((d + w, air - w, neighbor))
        memo[neighbor].append((d + w, air - w))


if bssf == oo:
    print("stuck")
else:
    print(bssf)
