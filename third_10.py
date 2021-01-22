import numpy as np
from utils import *
import time
import itertools

# PROJECT EULER 21
def euler21(N):
    def fsum(n):
        return np.array(get_factors(n,excl_N=True)).sum()

    skip = []
    ps = []
    for i in range(1,N+1):
        if i not in skip:
            a = fsum(i)
            b = fsum(a)
            if i != a and b == i:
                skip.append(a)
                ps.append(a)
                ps.append(b)
    return np.sum(ps)

# PROJECT EULER 22
def euler22():
    alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    inp = open('aux/e22.dat','r').readline().split(',')
    names = sorted([i[1:-1] for i in inp])

    def worth(n):
        w = 0
        for l in n: w+=(alph.index(l)+1)
        return w

    def score(n):
        return worth(n)*(names.index(n)+1)

    return np.array([score(n) for n in names]).sum()

# PROJECT EULER 23
def euler23():
    def get_abundant():
        out = []
        for i in range(1,28124):
            if np.array(get_factors(i,excl_N=True)).sum() > i:
                out.append(i)
        return np.array(out)

    out = 0
    abund = get_abundant()
    for i in range(1,28124):
        if len(np.intersect1d(abund,i-abund)) == 0: out+=i
            
    return out

# PROJECT EULER 24
def euler24():
    ans = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))[999999]
    out = ''
    for a in ans: out+=str(a)
    return out

# PROJECT EULER 25
def euler25(digits):
    done = False
    ind = 4
    fibos = [1,2]
    while not done:
        tm = [fibos[1],fibos[1]+fibos[0]]
        fibos = [i for i in tm]
        if len(str(tm[1])) >= digits:
            done = True
        else:
            ind += 1
    return ind

if __name__ == '__main__':
    # TWENTY ONE:
    st = time.time()
    print(f'Problem 21: {euler21(10000)} ({time.time()-st} s)')
    
    # TWENTY TWO:
    st = time.time()
    print(f'Problem 22: {euler22()} ({time.time()-st} s)')
    
    # TWENTY THREE:
    st = time.time()
    print(f'Problem 23: {euler23()} ({time.time()-st} s)')

    # TWENTY FOUR:
    st = time.time()
    print(f'Problem 24: {euler24()} ({time.time()-st} s)')
    
    # TWENTY FIVE:
    st = time.time()
    print(f'Problem 25: {euler25(1000)} ({time.time()-st} s)')

    
