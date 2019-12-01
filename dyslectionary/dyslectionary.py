import sys

def do_group(group):
    rev = sorted([g[::-1] for g in group])
    maxlen = max([len(g) for g in rev])
    for i in range(len(rev)):
        print(rev[i][::-1].rjust(maxlen))

L = [l.strip() for l in sys.stdin.readlines()]
group = []
first = True
for i in range(len(L)):
    if L[i] != "":
        group.append(L[i])
    else:
        if not first:
            print("")
        first = False
        do_group(group)
        group = []

if len(group) > 0:
    print("")
    do_group(group)
