N = int(input())
nums = [int(input()) for x in range(N)]
L = nums[-1]
M = []
for i in range(1, L + 1):
    if i not in nums:
        M.append(i)

if len(M) == 0:
    print("good job")
else:
    for j in M:
        print(j)
