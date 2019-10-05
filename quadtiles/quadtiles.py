K = [int(x) for x in input()][::-1]

x = 0
y = 0
for level in range(len(K)):
    if K[level] == 3:
        x += 2**(level)
        y += 2**(level)
    elif K[level] == 2:
        y += 2**(level)
    elif K[level] == 1:
        x += 2**(level)
    else:
        pass
print(len(K), x, y)
