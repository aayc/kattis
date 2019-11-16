import sys

lines = sys.stdin.readlines()
rhyme = len(lines[0].split(" "))
N = int(lines[1])
names = lines[2:]

pos = 0
A = []
B = []
i = True

while names:
    p = (pos + rhyme) % len(names)
    if i == True:
        A.append(names[p].strip())
        del names[p]
        i = not i
    else:
        B.append(names[p].strip())
        del names[p]
        i = not i
    if len(names) == 0:
        break
    pos = p % len(names)

print(len(A))
for i in range(len(A)):
    print(A[len(A) - i - 1])

print(len(B))
for j in range(len(B)):
    print(B[len(B) - j - 1])

        
