import sys
M = {}
def compute(ops):
    if len(ops) == 3:
        return eval("4" + ops[0] + "4" + ops[1] + "4" + ops[2] + "4")
    elif len(ops) == 2:
        M[compute(ops + ("+",))] = ops + ("+",)
        M[compute(ops + ("-",))] = ops + ("-",)
        M[compute(ops + ("*",))] = ops + ("*",)
        M[compute(ops + ("//",))] = ops + ("//",)
    else:
        compute(ops + ("+",))
        compute(ops + ("-",))
        compute(ops + ("*",))
        compute(ops + ("//",))

compute(())
L = sys.stdin.readlines()
T = int(L[0])
for t in range(T):
    R = int(L[t + 1])
    if R in M:
        result = "4 " + M[R][0] + " 4 " + M[R][1] + " 4 " + M[R][2] + " 4 = " + str(R)
        result = result.replace("//", "/")
        print(result)
    else:
        print("no solution")

