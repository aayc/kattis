T = int(input())
for t in range(T):
    input()
    N = int(input())
    sm = 0
    for i in range(N):
        sm += int(input())
    if sm % N == 0:
        print("YES")
    else:
        print("NO")

