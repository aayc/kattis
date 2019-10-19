input()
V = [True if x == "T" else False for x in input().split(" ")]
L = input().split(" ")

q = []
ops = ["+", "-", "*"]

def convert(sym, V):
    if type(sym) is str:
        v = V[ord(sym) - 65]
    else:
        v = sym
    return v

for c in L:
    if c not in ops:
        q.append(c)
    else:
        if c == "-":
            v = convert(q.pop(), V)
            q.append(not v)
        elif c == "+":
            v1 = convert(q.pop(), V)
            v2 = convert(q.pop(), V)
            q.append(v1 or v2)
            
        elif c == "*":
            v1 = convert(q.pop(), V)
            v2 = convert(q.pop(), V)
            q.append(v1 and v2)

print("T" if convert(q[0], V) else "F")
            
            
            

