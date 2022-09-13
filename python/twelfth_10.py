import numpy as np
import utils
import time
import copy

def euler111():
    return 'Not solved'

# This one is probably way longer than necessary...
# was going to do some clever stuff to optimise, but it's not that slow so whatever (see 113)
def euler112(target=0.5):
    def add_one(n):
        ind = -1
        while True:
            if n[ind] != 9:
                n[ind]+=1
                break
            else:
                n[ind] = 0
                ind -= 1
        return n

    def calc_perc(b,n):
        N = ''
        for _ in n: N+=str(_)
        return b/float(N)

    n = [1,0,0]
    b = 0
    while calc_perc(b,n) < target:
        if all([_ == 9 for _ in n]):
            n = [1] + [0]*len(n)
        n = add_one(n)
        i = 0
        while True:
            if n[i] == n[i+1]:
                i+=1
                if i == len(n)-1: break
                continue
            sd = 'd' if n[i] > n[i+1] else 'u'
            break
        
        i+=1
        bounce = False
        while True:
            if i >= len(n)-1: break
            if n[i] == n[i+1]:
                i+=1 
                if i == len(n)-1: break
                continue
            nd = 'd' if n[i] > n[i+1] else 'u'
            if sd != nd:
                bounce = True
                break
            i+=1
        if bounce: b+=1
    ans = ''
    for _ in n: ans+=str(_)
    return int(ans)

def euler113():
    def combs(n,r):
        num = utils.factorial(n)
        den = utils.factorial(r)*utils.factorial(n-r)
        return num/den

    return int(combs(110,10) + combs(109,9) - 2 - 10*100)

def euler114(N=7):
    cache = [0]*(N+1)
    def F(N,n):
        out=1
        if n > N:
            return out
        if cache[N] != 0:
            return cache[N]
        for s in range(N-n+1):
            for b in range(n,N-s+1):
                out += F(N-s-b-1,n)

        cache[N] = out
        return out

    return F(N,3)  

def euler115(m=3):
    cache = {}
    def F(N,n):
        out=1
        if n > N:
            return out
        if N in cache.keys():
            return cache[N]
        for s in range(N-n+1):
            for b in range(n,N-s+1):
                out += F(N-s-b-1,n)

        cache[N] = out
        return out
    
    N = 15
    while True:
        cv = F(N,m)
        if cv > 1e6:
            break
        N+=1
    return N

def euler116(N=5):
    cache = {}
    def F(N,n):
        out=0
        if n > N:
            return out
        if N in cache.keys():
            return cache[N]
        for s in range(N-n+1):
            out += F(N-s-n,n)+1

        cache[N] = out
        return out

    out = 0
    for _ in [2,3,4]:
        cache = {}
        out += F(N,_)
    return out

def euler120():
    ans = 0
    x = 2
    for a in range(3,1001):
        ans += x*a
        if a%2 == 0: x+=2
    return ans

if __name__ == '__main__':

    # ONE HUNDRED AND ELEVEN:
    st = time.time()
    print(f'Problem 111: {euler111()} ({time.time()-st} s)')

    # ONE HUNDRED AND TWELVE:
    st = time.time()
    print(f'Problem 112: {euler112(.99)} ({time.time()-st} s)')
    
    # ONE HUNDRED AND THIRTEEN:
    st = time.time()
    print(f'Problem 113: {euler113()} ({time.time()-st} s)')

    # ONE HUNDRED AND FOURTEEN
    st = time.time()
    print(f'Problem 114: {euler114(50)} ({time.time()-st} s)')

    # ONE HUNDRED AND FIFTEEN
    st = time.time()
    print(f'Problem 115: {euler115(50)} ({time.time()-st} s)')
    
    # ONE HUNDRED AND SIXTEEN
    st = time.time()
    print(f'Problem 116: {euler116(50)} ({time.time()-st} s)')

    # ONE HUNDRED AND TWENTY:
    st = time.time()
    print(f'Problem 120: {euler120()} ({time.time()-st} s)')