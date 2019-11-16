N = int(input())
prices = [int(x) for x in input().split(" ")]
M = int(input())
toppings = [int(x) for x in input().split(" ")]
combos = []
gmin = float("inf")
for i in range(N):
    combo = [int(x) for x in input().split(" ")]
    for c in combo:
        gmin = min(gmin, toppings[c - 1] + prices[i])


# find the min combination
X = int(input())
print( max(X // gmin - 1, 0))

