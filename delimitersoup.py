from collections import deque
input()
L = input()
s = deque([])
matching = {
        ")":"(",
        "]":"[",
        "}":"{"
        }
for i in range(len(L)):
    if L[i] in ["(", "[", "{"]:
        s.append(L[i])
    elif L[i] in [")", "]", "}"]:
        c = s.pop()

