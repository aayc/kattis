import sys
import time

start_time = time.time()

from random import randint
a = [randint(0, 5000) for i in range(5000)]
for i in range(5000):
    b = sorted(a)
print("elapsed", time.time() - start_time)
