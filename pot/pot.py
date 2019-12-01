N = int(input())
nums = [input() for i in range(N)]
ns = [int(n[:len(n) - 1])**(int(n[-1])) for n in nums]
print(sum(ns))
