n = int(input())
names = []
for i in range(n):
    names.append(input())

alphabetic_forward = True
def m(names):
    for i in range(1, len(names)):
        if names[i] < names[i - 1]:
            return False
    return True

if m(names):
    print("INCREASING")
elif m(names[::-1]):
    print("DECREASING")
else:
    print("NEITHER")

