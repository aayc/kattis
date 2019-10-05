def solution(board):
    nk = 0
    # iterate through all the squares
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == "k":
                nk += 1
                # check if it fights any other knight
                positions = [[r + 2, c - 1],
                             [r + 2, c + 1],
                             [r - 2, c - 1],
                             [r - 2, c + 1],
                             [r + 1, c - 2],
                             [r + 1, c + 2],
                             [r - 1, c + 2],
                             [r - 1, c - 2]]

                for nr, nc in positions:
                    if 0 <= nr < len(board) and 0 <= nc < len(board[r]):
                        if board[nr][nc] == "k":
                            return "invalid"
    return "valid" if nk == 9 else "invalid"




T = int(input())
for t in range(T):
    if t != 0:
        _ = input()
    board = [list(input()) for i in range(5)]
    print(solution(board))
