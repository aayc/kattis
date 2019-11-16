import sys

def execute(ins):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = 0
    x = 0
    y = 0

    for move in ins:
        if move == "Forward":
            x += directions[d][0]
            y += directions[d][1]
        elif move == "Left":
            d -= 1
            if d < 0:
                d = 3
        elif move == "Right":
            d += 1
            d = d % len(directions)
    return (x, y)



L = sys.stdin.readlines()
X, Y = [int(x) for x in L[0].split(" ")]
instructions = [l.strip() for l in L[2:]]
types = ["Left", "Forward", "Right"]
for i in range(len(instructions)):
    original = instructions[i]
    is_wrong = False
    for t in types:
        if original != t:
            instructions[i] = t
            result = execute(instructions)
            if (X, Y) == result:
                print(i + 1, t)
                is_wrong = True
                break
    instructions[i] = original
    if is_wrong:
        break

