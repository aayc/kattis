L, W = [int(x) for x in input().split(" ")]
lanes = [[int(x) for x in input().split(" ")] for x in range(L)]
S, moves = input().split(" ")
S = int(S)

def draw_grid(L, W, lanes):
    grid = [[0 for j in range(W)] for i in range(L)]
    left_lanes = lanes[::2]
    right_lanes = lanes[1::2]
    for i, (offset, interval, speed) in enumerate(left_lanes):
        grid[2*i][offset] #basically fill the grid where it's unsafe to be at time t
        # the only difference in time is t
        #
    return grid

def froggie(L, W, lanes, S, moves):
    grid = draw_grid(L, W, lanes)
    r, c = (S, len(grid) - 1)
    for m in moves:
        if m == "R":
            c += 1
        elif m == "L":
            c -= 1
        elif m == "U":
            r -= 1
        else:
            r += 1

        if r < 0:
            return "safe"
        elif grid[r][c] == 1:
            return "squished"

        for i in range(len(lanes)):
            lanes[i][0] = (lanes[i][0] + lanes[i][2]) % W
        grid = draw_grid(L, W, lanes)
    return "squished"
