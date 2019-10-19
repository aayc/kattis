from random import randint, shuffle

N = 500
M = 500 * 100
T = 100
A = int(2e6)
visited = set()
rest_stops = (list(range(2, N)))
shuffle(rest_stops)
rest_stops = rest_stops[:T]

i = 0
lines = []
while i < M:
    f = randint(1, N)
    t = randint(1, N)
    if (f, t) in visited or (t, f) in visited:
        continue

    visited.add((f, t))
    visited.add((t, f))

    w = randint(1000, 3e6)
    lines.append((f, t, w))
    i += 1

with open("input5.txt", "w") as f:
    f.write(f"{N} {M} {T} {A}\n")
    f.write(" ".join([str(s) for s in rest_stops]) + "\n")
    for a, b, c in lines:
        f.write(f"{a} {b} {c}\n")
