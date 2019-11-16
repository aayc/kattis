import sys

L = sys.stdin.readlines()[1:]
for i in range(len(L)):
    students = [int(x) for x in L[i].split(" ")[1:]]
    total = 0
    for j in range(len(students)):
        for k in range(j + 1, len(students)):
            if students[j] > students[k]:
                total += 1
    print(i + 1, total)

