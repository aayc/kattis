import sys

instructions = [l.strip() for l in sys.stdin.readlines()]
r = 0
c = 0
pathr = [r]
pathc = [c]
for ins in instructions:
    if ins == "down":
        r += 1
    elif ins == "left":
        c -= 1
    elif ins == "right":
        c += 1
    else:
        r -= 1
    pathr.append(r)
    pathc.append(c)


# normalize path
mr = min(pathr)
mc = min(pathc)
pathr = [r - mr for r in pathr]
pathc = [c - mc for c in pathc]
pathset = set(tuple(zip(pathr, pathc)))
height = max(pathr) + 1
length = max(pathc) + 1
M = [["*" if (r, c) in pathset else " " for c in range(length)] for r in range(height)]
M[pathr[0]][pathc[0]] = "S"
M[pathr[-1]][pathc[-1]] = "E"
print("#" * (length + 2))
for r in range(len(M)):
    print("#" + "".join(M[r]) + "#")
print("#" * (length + 2))



        

