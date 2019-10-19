import math

N = int(input())
for i in range(N):
    w, g, h, r = [int(x) for x in input().split(" ")]
    gp = g - r
    hp = h - r

    a1 = math.sqrt((gp - hp)**2 + w**2)
    a2 = math.sqrt((gp + hp)**2 + w**2)

    print("{0:.8f} {1:.8f}".format(a1, a2))
