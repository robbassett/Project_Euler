import numpy as np

def factorial(N):
    return int(np.linspace(1,N,N).prod())

def big_factorial(N):
    V = [1]
    carry = 0
    for n in np.linspace(2,N,N-1):
        for i,v in enumerate(V):
            carry,t = divmod(v*n + carry,10)
            V[i] = t
        if carry != 0:
            for c in str(int(carry))[::-1]:
                V = V+[int(c)]
            carry = 0
    return V
            

def fibonacci(Nterms):
    out = np.zeros(Nterms)
    out[0],out[1] = 1,2
    for i in range(Nterms-2):
        out[i+2] = out[i]+out[i+1]
    return out

def primes_lt_n(n):
    """ Returns  a list of primes < n """
    n = int(n)
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return np.array([2] + [2*i+1 for i in range(1,n//2) if sieve[i]])

def n_primes(n):
    """ Returns first n primes """
    p = [2]
    c = 2
    while len(p) < n:
        j = 0
        c += 1
        while j < len(p):
            if c % p[j] == 0:
                break
            elif j == len(p) - 1:
                p.append(c)
            j += 1
    return p

def get_factors(n):
    fcts = []
    for i in range(int(np.sqrt(n))):
        if n%(i+1) == 0:
            fcts.append(i+1)
            if (n/(i+1)) not in fcts:
                fcts.append(n/(i+1))
    return fcts
