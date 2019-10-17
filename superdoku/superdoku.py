N, K = [int(x) for x in input().split(" ")]
grid = [[int(x) for x in input().split(" ")] for i in range(K)]
grid += [[-1 for j in range(N)] for i in range(N - K)]
row_repr = [set(grid[r]) for r in range(N)]
col_repr = [set([grid[r][c] for r in range(N)]) for c in range(N)]

def solver(grid, r = 0, c = 0):
    if r == N:
        return grid

    nr = r + 1 if c == len(grid[r]) - 1 else r
    nc = c + 1 if c != len(grid[r]) - 1 else 0

    if grid[r][c] == -1:
        for i in range(1, N + 1):
            if i not in row_repr[r] and i not in col_repr[c]:
                grid[r][c] = i
                row_repr[r].add(i)
                col_repr[c].add(i)

                ans = solver(grid, nr, nc)
                if ans is not None:
                    return ans

                row_repr[r].remove(i)
                col_repr[c].remove(i)
                grid[r][c] = -1
        return None
    else:
        return solver(grid, nr, nc)


res = solver(grid)
if res is None:
    print("no")
else:
    print("yes")
    for g in res:
        print(*g)
