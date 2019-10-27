import sys


L = sys.stdin.readlines()
N = int(L[0])
strings = []
for i in range(N):
    strings.append([L[i + 1].rstrip()])
last = 0
for j in range(N - 1):
    command = L[N + 1 + j]
    a, b = [int(x) - 1 for x in command.split(" ")]
    strings[a] = strings[a] + strings[b]
    strings[b] = ""
    last = a
print("".join(strings[last]))

'''
N = int(input())
strings = [input() for i in range(N)]
last = 0
for j in range(N - 1):
    a, b = [int(x) - 1 for x in input().split(" ")]
    strings[a] = strings[a] + strings[b]
    last = a
print(strings[last])
''' 
