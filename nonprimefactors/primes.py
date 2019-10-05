import math
import functools
import itertools
from copy import deepcopy
Q = int(input())
ns = [int(input()) for x in range(Q)]
memo = {}

def gen_primes():
    primes = [2, 3, 5]
    for i in range(6, 1415):
        limit_i = math.sqrt(i) + 1
        j = 0
        while primes[j] < limit_i and j < len(primes):
            if i % primes[j] == 0:

                break
            j += 1
        else:
            primes.append(i)


    return primes
primes = gen_primes()

def merge(a, b):
    for k, v in a:
        b[k] = b.get(k, 0) + v
    return b


def factorize(N, f = 0):

    global primes

    if f == len(primes):
        return {}
    if N in memo:
        return memo[N]
    if N == 1:
        return {}
    else:
        factors = {}
        if N % primes[f] == 0:
            factors = factorize(N // primes[f], f)
            factors[primes[f]] = factors.get(primes[f], 0) + 1
            memo[N] = deepcopy(factors)
            return factors
        else:
            factors = factorize(N, f + 1)
            memo[N] = deepcopy(factors)
            return factors


def solution(N):
    factors = factorize(N)
    if factors is None:
        return 1
    f_freq = [n + 1 for n in factors.values()]
    prod = functools.reduce(lambda x, y: x * y, f_freq, 1)
    prod -= len(f_freq)
    return prod

for n in ns:
    print(solution(n))

#print(factorize(100))
#print(factorize(50))
#print(factorize(8000))
