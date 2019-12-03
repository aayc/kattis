T = int(input())
for t in range(T):
    D, M = [int(x) for x in input().split(" ")]
    ds = [int(x) for x in input().split(" ")]
    # 0 1M 2T 3W 4Th 5F 6S
    day = 0
    daycount = 1
    count = 0
    j = 0
    for i in range(1, D + 1):
        if daycount == ds[j] + 1:
            j += 1
            daycount = 1
        if daycount == 13 and day == 5:
            count += 1
        daycount += 1
        day = (day + 1) % 7
    print(count)

