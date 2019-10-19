P, D = [int(x) for x in input().split(" ")]
A = [0 for i in range(D)]
B = [0 for i in range(D)]

for i in range(P):
    d, a, b = [int(x) for x in input().split(" ")]
    A[d - 1] += a
    B[d - 1] += b

i = 1
wa = 0
wb = 0
for a, b in zip(A, B):
    #print("----")
    #print(i, a, b)
    
    if a > b:
        lost_a = a - ((a + b) // 2 + 1)
        lost_b = b
        win = "A"
    else:
        lost_a = a
        lost_b = b - ((a + b) // 2 + 1)
        win = "B"
    print(win, lost_a, lost_b)
    wa += lost_a
    wb += lost_b
    i += 1

print("{0:.10f}".format(abs(wa - wb) / (sum(A) + sum(B))))

    
