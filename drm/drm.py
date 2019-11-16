m = input()

def v(c):
    return ord(c) - 65

a = m[0:len(m) // 2]
b = m[len(m) // 2:]

sa = sum([v(c) for c in a])
sb = sum([v(c) for c in b])
a = [chr(((v(c) + sa) % 26) + 65) for c in a]
b = [chr(((v(c) + sb) % 26) + 65) for c in b]
result = [chr(((v(a[i]) + v(b[i])) % 26) + 65) for i in range(len(a))]
print("".join(result))
