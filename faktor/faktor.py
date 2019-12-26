import math
A, I = [int(x) for x in input().split(" ")]
M = A * I
while math.ceil(M / A) >= I:
    M -= 1
M += 1
print(M)
