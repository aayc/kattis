import sys
import bisect
L = [int(x) for x in sys.stdin.readlines()]
case = 1
while len(L) > 0:
    N = L[0]
    nums = L[1:N + 1]
    sums = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sums.append(nums[i] + nums[j])
    sums = sorted(set(sums))

    L = L[N + 1:]
    M = L[0]
    queries = L[1:M + 1]

    print(f"Case {case}:")
    for q in queries:
        ix = bisect.bisect_left(sums, q)
        closest = 0
        if ix == len(sums):
            closest = sums[-1]
        elif ix == 0:
            closest = sums[ix]
        else:
            after = sums[ix]
            before = sums[ix - 1]
            if after - q < q - before:
                closest = after
            else:
                closest = before
        print(f"Closest sum to {q} is {closest}.")

    L = L[M + 1:]
    case += 1

