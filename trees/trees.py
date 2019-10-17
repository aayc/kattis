from collections import Counter

trees = {}
n = 0
while True:
    try:
        m = input()
        if m in trees:
            trees[m] += 1
        else:
            trees[m] = 1
        n += 1
    except:
        break

results = []
for k, v in trees.items():
    results.append((k, v / n * 100))
results = sorted(results, key=lambda x: x[0])

for r in results:
    print(r[0], "{0:.6f}".format(r[1]))
