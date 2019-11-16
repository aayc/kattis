# DONE
import sys
L = [l.strip() for l in sys.stdin.readlines()]
prev_name = L[0]
names = L[2:]

starts_with = {}
ends_with = {}

for name in names:
    if name[0] not in starts_with:
        starts_with[name[0]] = []
    if name[-1] not in ends_with:
        ends_with[name[-1]] = []

    starts_with[name[0]].append(name)
    ends_with[name[-1]].append(name)


e = prev_name[-1]
if e not in starts_with:
    print("?")
    sys.exit(0)

candidates = [m for m in starts_with[e] if m != prev_name] # O(n)
saving = ""

for i in range(len(candidates)):
    if candidates[i][-1] in starts_with:
        next_names = starts_with[candidates[i][-1]]
        if len(next_names) == 0 or (len(next_names) == 1 and next_names[0] == candidates[i]):
            print(candidates[i] + "!")
            sys.exit(0)
        elif saving == "":
            saving = candidates[i]

        # determine if THAT starts_with exists in ends_with, and if it does then it's good but if it doesn't it's better and output immediately
    else:
        print(candidates[i] + "!")
        sys.exit(0)

if saving != "":
    print(saving)
else:
    print("?")



    


