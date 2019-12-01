N = int(input())
for i in range(N):
    nums = [int(x) for x in input().split(" ")]
    if nums[1] - nums[2] > nums[0]:
        print("advertise")
    elif nums[1] - nums[2] == nums[0]:
        print("does not matter")
    else:
        print("do not advertise")

