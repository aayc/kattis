def sol(grades):
    N = len(grades)
    avg = sum(grades) / len(grades)
    G = sum([g > avg for g in grades])
    P = round(G / N * 100, 3)
    print("%.3f%s" % (round(G / N * 100, 3), '%'))

T = int(input())
for t in range(T):
    L = input()
    sol([int(x) for x in L.split(" ")][1:])
