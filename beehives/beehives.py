import math

def dist(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2

while True:
    d, N = input().split(" ")
    d = float(d)
    N = int(N)
    if N == 0:
        break

    hives = []
    for i in range(N):
        x, y = [float(f) for f in input().split(" ")]
        hives.append((x, y))

    sweet = 0
    sour = 0
    d = d **2
    for i in range(len(hives)):
        for j in range(len(hives)):
            if i == j:
                continue

            ds = dist(hives[i], hives[j])
            if ds <= d:
                sour += 1
                break
        else:
            sweet += 1


    print(sour, "sour,",  sweet, "sweet")
