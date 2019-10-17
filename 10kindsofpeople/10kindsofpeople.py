from collections import deque


def solution(a, b, y, z):
    q = deque([(a, b)])
    V = set()
    while q:
        r, c = q.popleft()
        if r == y and c == z:
            return True

        neighbors = [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]
        for neighbor in neighbors:
            nr, nc = neighbor
            if 0 <= nr < len(M) and 0 <= nc < len(M[0]) and (nr, nc) not in V and M[nr][nc] == M[r][c]:
                V.add((nr, nc))
                q.append((nr, nc))

    return False

def dfs(r, c, V):


R, C = [int(x) for x in input().split(" ")]
M = []
for i in range(R):
    M.append(list(input()))

L = []


T = int(input())
for t in range(T):
    a, b, c, d = [int(x) for x in input().split(" ")]
    user = "decimal" if M[a - 1][b - 1] == '1' else "binary"
    if solution(a - 1, b - 1, c - 1, d - 1):
        print(user)
    else:
        print("neither")
