O, s = input().split(" ")
ret = ""
if O == "E":
    i = 0
    c = s[i]
    count = 0
    while i < len(s):
        if s[i] == c:
            count += 1
        else:
            ret += c + str(count)
            c = s[i]
            count = 1
        i += 1
    ret += c + str(count)
else:
    for i in range(0, len(s), 2):
        ret += s[i] * int(s[i + 1])
print(ret)
