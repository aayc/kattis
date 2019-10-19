input()
Ns = [int(x) for x in input().split(" ")]

lr = 0
sumlr = 0
rl = 0
sumrl = 0
for i in range(len(Ns)):
    sumrl += Ns[len(Ns) - i - 1]
    rl = max(rl, sumrl / (i + 1))

    sumlr += Ns[i]
    lr = max(lr, sumlr / (i + 1))


print("{0:.9f}".format(max(lr, rl, 0)))
