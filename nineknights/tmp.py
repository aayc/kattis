def solution(board):
    nk = 0
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == "k":
                nk += 1
                can_reach = [[r + 2, c - 1],
                             [r + 2, c + 1],
                             [r - 2, c - 1],
                             [r - 2, c + 1],
                             [r + 1, c - 2],
                             [r + 1, c + 2],
                             [r - 1, c + 2],
                             [r - 1, c - 2]]

                for nr, nc in can_reach:
                    if 0 <= nr < len(board) and 0 <= nc < len(board[r]) and board[nr][nc] == "k":
                        return "invalid"
    return "valid" if nk == 9 else "invalid"



T = int(input())

for t in range(T):
    if t != 0:
        _ = input()
    board = [list(input()) for i in range(5)]
    print(solution(board))

def plus_size(board, r, c):
    R = 1
    while True:
        positions = [[r + R, c], [r - R, c], [r, c + R], [r, c - R]]
        for nr, nc in positions:
            if 0 <= etc etc etc
        R += 1
