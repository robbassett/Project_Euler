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
    inp = open('dat/e22.dat','r').readline().split(',')
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

# PROJECT EULER 26
def euler26(N):
    mx = 0
    ans = 0
    for i in range(2,N+1):
        done = False
        t = 1
        rems = []
        while not done:
            r = t%i
            if r == 0:
                done = True
                recur = 0
            else:
                if r not in rems:
                    rems.append(r)
                    t = 10*r
                else:
                    done = True
                    recur = len(rems)
        if recur > mx:
            mx = recur
            ans = i
    return ans

# PROJECT EULER 27
def euler27(mx):
    def quad(n,a,b):
        return n*n + n*a + b
    
    cprimes = primes_lt_n(1000000)
    bprimes = primes_lt_n(mx)
    mxl = 0
    a0,b0 = 0,0
    for a in range(-mx,mx):
        for b in bprimes:
            c = 0
            n = 0
            ns = []
            ps = []
            done = False
            while not done:
                c += 1
                n += 1
                if quad(n,a,b) in cprimes:
                    ns.append(n)
                    ps.append(quad(n,a,b))
                else:
                    done = True
            if c > mxl:
                mxl = c
                a0,b0 = a,b
    return a0*b0

# PROJECT EULER 28
def euler28(N):
    out = 1
    v = 1
    for s in range(3,N+2,2):
        for i in range(4):
            v += (s-1)
            out += v
    return out

# PROJECT EULER 29
def euler29(lo,hi):
    out = []
    for a in range(lo,hi+1):
        for b in range(lo,hi+1):
            t = a**b
            if t not in out: out.append(t)
    return len(out)

# PROJECT EULER 30:
def euler30(P):
    nums = []
    ps = np.linspace(0,9,10)**P
    done = False
    st = 2
    while not done:
        tm = np.array([ps[int(i)] for i in str(st)]).sum()
        if st == tm: nums.append(st)
        if st > 200000:
            done = True
        st+=1
    return np.sum(nums)

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
    
    # TWENTY SIX:
    st = time.time()
    print(f'Problem 26: {euler26(1000)} ({time.time()-st} s)')
    
    # TWENTY SEVEN:
    st = time.time()
    print(f'Problem 27: {euler27(1000)} ({time.time()-st} s)')

    # TWENTY EIGHT:
    st = time.time()
    print(f'Problem 28: {euler28(1001)} ({time.time()-st} s)')

    # TWENTY NINE:
    st = time.time()
    print(f'Problem 29: {euler29(2,100)} ({time.time()-st} s)')

    # THIRTY:
    st = time.time()
    print(f'Problem 30: {euler30(5)} ({time.time()-st} s)')
    
