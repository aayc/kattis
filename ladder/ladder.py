import math
opp, ang = [int(x) for x in input().split(" ")]
print(math.ceil(opp / math.sin(math.radians(ang))))
