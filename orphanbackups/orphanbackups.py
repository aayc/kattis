import sys

L = sys.stdin.readlines()
fnames = set()
accounted = set()
start_ix = -1
for i in range(len(L)):
    l = L[i].strip()
    if l == "":
        start_ix = i
        break
    else:
        fnames.add(l)

unaccounted = []
for i in range(start_ix + 1, len(L)):
    l = L[i].strip().split("_")
    ll = "".join(l[:len(l) - 2])
    if ll in fnames:
        fnames.remove(ll)
        accounted.add(ll)
    elif ll in accounted:
        continue
    else:
        unaccounted.append(L[i].strip())

for s in sorted(unaccounted):
    print("F", s)

for s in sorted(list(fnames)):
    print("I", s)

if len(unaccounted) == 0 and len(fnames) == 0:
    print("No mismatches.")
