import numpy as np
from utils import *

# PROJECT EULER 1
def natural_numbers_below(N):
    out = 0
    for i in range(1,N):
        if i%3 == 0 or i%5 == 0: out+=i
    return out

# PROJECT EULER 2
def even_fibo_sum(max_val):
    fibo = np.zeros(1)
    i = 3
    while fibo.max() < max_val:
        i+=1
        fibo = fibonacci(i)
    t = np.where(fibo%2 == 0)[0]
    return fibo[t].sum()

# PROJECT EULER 3
def largest_prime_factor(N):
    p = primes(int(np.sqrt(N)))
    v = np.where(N%p == 0)[0]
    return p[int(v.max())]

if __name__ == '__main__':
    # ONE:
    ans = natural_numbers_below(1000)
    print(f'Problem 1: {ans}')

    # TWO:
    ans = even_fibo_sum(4.e6)
    print(f'Problem 2: {int(ans)}')

    # THREE:
    ans = largest_prime_factor(600851475143)
    print(f'Problem 3: {ans}')

    
