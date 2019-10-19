import math

a, b = [int(x) for x in input().split(" ")]
g = math.gcd(a, b)
if (a // g) % 2 != 0 and (b // g) % 2 != 0:
    print(g)
else:
    print(0)
