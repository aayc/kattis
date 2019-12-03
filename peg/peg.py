N = 7
board = [list(input()) for i in range(N)]

def crit(board, r, c, shape):
    if 0 <= r < len(board) and 0 <= c < len(board[r]):
        return board[r][c] == shape
    else:
        return False

moves = 0
for r in range(len(board)):
    for c in range(len(board[r])):
        if board[r][c] == "o":
            if crit(board, r + 1, c, "o") and crit(board, r + 2, c, "."):
                moves += 1
            if crit(board, r - 1, c, "o") and crit(board, r - 2, c, "."):
                moves += 1
            if crit(board, r, c + 1, "o") and crit(board, r, c + 2, "."):
                moves += 1
            if crit(board, r, c - 1, "o") and crit(board, r, c - 2, "."):
                moves += 1
print(moves)
