from collections import deque

secret, s = input().split(" ")
secret = deque(secret)
M = set(secret)
j = 0
for i in range(len(s)):
    if len(secret) > 0 and s[i] == secret[0]:
        secret.popleft()
        M = set(secret)
    elif s[i] in M:
        print("FAIL")
        break
else:
    if j == len(secret):
        print("PASS")
    else:
        print("FAIL")

