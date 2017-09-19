def primes(rangeLimit):
    n = rangeLimit+1
    primes = dict()
    for i in range(2, n): primes[i] = True
    for i in primes:
        factors = range(i,n, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]
print(primes(10000))