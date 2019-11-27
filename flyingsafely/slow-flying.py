T = int(input())

def dfs(node, V):
    edges = 0
    for neighbor in range(N):
        if neighbor not in V and A[node][neighbor]:
            edges += 1
            V.add(neighbor)
            edges += dfs(neighbor, V)
    return edges
for t in range(T):
    N, M = [int(x) for x in input().split(" ")]
    A = [[False for i in range(N)] for j in range(N)]

    for i in range(M):
        a, b = [int(x) for x in input().split(" ")]
        A[a - 1][b - 1] = True
        A[b - 1][a - 1] = True


    ans = dfs(0, set([0]))
    print(ans)
                
