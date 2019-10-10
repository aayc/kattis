N, P, C = [int(x) for x in input().split(" ")]
pills = [[int(x) for x in input().split(" ")] for i in range(P)]

# DP, over the number of seconds that have passed
# seconds is very high, can't use it as a dimension
# 10**5 pills
#
# you can either take a pill and not take any other pills but inc your time
# or you can not take the pill and keep your time
