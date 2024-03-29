import numpy as np
from utils import *
import matplotlib.pyplot as plt
import itertools
import time

# PROJECT EULER 31
def euler31(total):
    coins = [1,2,5,10,20,50,100,200]
    combs = np.zeros((total+1,len(coins)))
    for v in range(combs.shape[0]):
        target = v+1
        for i,c in enumerate(coins):
            ind = target-c-1
            if ind < 0: ind += len(combs)
            if i == 0: combs[v][i] = 1
            elif c <= target:
                combs[v][i] = combs[v][i-1] + combs[ind][i]
            else:
                combs[v][i] = combs[v][i-1]
    return int(combs[-1][-1])

# PROJECT EULER 32
def euler32():
    its = np.array(list(itertools.permutations([1,2,3,4,5,6,7,8,9])))
    nums = []
    for it in its:
        for t in [1,2]:
            a = ''
            for i in range(t): a+=str(it[i])
            b = ''
            for i in range(t,5): b+=str(it[i])
            c = ''
            for i in range(5,len(it)): c+=str(it[i])
            if int(a)*int(b) == int(c) and int(c) not in nums:
                nums.append(int(c))
    return np.sum(nums)

# PROJECT EULER 33
def euler33():
    dens = []
    nums = []
    for d in range(11,99):
        for n in range(10,d):
            if str(n)[1] == '0' and str(d)[1] == '0':
                pass
            else:
                if str(n)[0] in str(d) or str(n)[1] in str(d):
                    if str(n)[0] in str(d):
                        nn = int(str(n)[1])
                        if str(n)[0] == str(d)[0]:
                            dd = int(str(d)[1])
                        else:
                            dd = int(str(d)[0])
                    else:
                        nn = int(str(n)[0])
                        if str(n)[1] == str(d)[0]:
                            dd = int(str(d)[1])
                        else:
                            dd = int(str(d)[0])
                    try:
                        if n/d == nn/dd:
                            dens.append(dd)
                            nums.append(nn)
                    except:
                        pass
    return int(np.prod(dens)/np.prod(nums))

# PROJECT EULER 34:
def euler34():
    def fact_sum(n):
        return np.sum([factorial(int(d)) for d in str(n)])
    v = 0
    for N in range(3,50000):
        if N == fact_sum(N): v+=N
    return v

# PROJECT EULER 35:
def euler35(N):
    primes = primes_lt_n(N+1)
    circs = 0
    skip = []
    for prime in primes:
        if prime < 10:
            circs+=1
        elif prime in skip:
            pass
        else:
            fl = 0
            p = [str(prime)[i] for i in range(len(str(prime)))]
            pp = []
            inds = np.linspace(0,len(str(prime))-1,len(str(prime))).astype(int)
            for i in range(len(str(prime))-1):
                inds = (inds+1)%len(str(prime))
                t = ''
                for j in inds: t+=p[j]
                if int(t) not in primes:
                    fl = 1
                    break
                else:
                    if int(t) != prime:
                        pp.append(int(t))
                   
            if fl == 0:
                skip.append(prime)
                circs += 1
                for p in pp:
                    skip.append(p)
                    circs += 1
    return circs

# PROJECT EULER 36:
def euler36(mx):
    ans = 0
    for i in range(0,mx):
        b = np.binary_repr(i)
        if str(i) == str(i)[::-1] and b == b[::-1]: ans+=i
    return ans

# PROJECT EULER 37:
def euler37(n):
    p = [2]
    c = 2
    trunc = []
    while len(trunc) < n:
        j = 0
        c += 1
        while j < len(p):
            if c % p[j] == 0:
                break
            elif j == len(p) - 1:
                p.append(c)
            j += 1

        if p[-1] > 7 and p[-1] not in trunc and int(str(p[-1])[:2]) in p:
            tp = str(p[-1])
            f = 0
            for g in range(1,len(tp)):
                if int(tp[g:]) not in p or int(tp[:-g]) not in p:
                    f = 1
                    break
            if f == 0:
                trunc.append(int(tp))
            
    return np.sum(trunc)

# PROJECT EULER 38:
def euler38():
    def l2n(l):
        n = ''
        for i in l: n +=str(i)
        return int(n)
    def n2l(n):
        return [int(i) for i in str(n)]
    
    pdn = list(itertools.permutations([1,2,3,4,5,6,7,8,9]))[::-1]
    for t in pdn:
        for i in range(1,len(t)):
            fl = 1
            l1 = n2l(l2n(t[:i]))
            l2 = n2l(l2n(t[:i])*2)
            ch = n2l(l2n(t[i:i+len(l2)]))
            if l2 == ch:
                i2 = i+len(l2)
                f = 3
                done = False
                if i2 == 9:
                    fl = 0
                    done = True
                while not done:
                    tl = n2l(l2n(t[:i])*f)
                    try:
                        if n2l(l2n(t[i2:i2+len(tl)])) == tl:
                            if i2+len(tl) >= 9:
                                fl = 0
                                done = True
                            else:
                                i2 += len(tl)
                                f += 1
                        else:
                            done = True
                    except:
                        done = True
            if fl == 0:
                break
        if fl == 0:
            out = l2n(t)
            break
    return out

# PROJECT EULER 39:
def euler39(mx):
    def get_combos(p):
        cs = []
        for a in range(1,int(p/3)):
            for b in range(a,int(2*p/3)):
                c = np.sqrt(a*a + b*b)
                if a + b + c == p:
                    cs.append([a,b,int(c)])
        return cs

    ans = 0
    m = 0
    for i in range(10,mx+1):
        cc = get_combos(i)
        if len(cc) > m:
            ans = i
            m = len(cc)

    return ans

# PROJECT EULER 40:
def euler40(l):
    n = ''
    i=1
    while len(n) < max(l):
        n+=str(i)
        i+=1
    out = np.zeros(len(l))
    for i,v in enumerate(l): out[i] = int(n[v-1])

    return int(np.prod(out))

if __name__ == '__main__':
    # THIRTY ONE:
    st = time.time()
    print(f'Problem 31: {euler31(200)} ({time.time()-st} s)')
    
    # THIRTY TWO:
    st = time.time()
    print(f'Problem 32: {euler32()} ({time.time()-st} s)')
    
    # THIRTY THREE:
    st = time.time()
    print(f'Problem 33: {euler33()} ({time.time()-st} s)')
    
    # THIRTY FOUR:
    st = time.time()
    print(f'Problem 34: {euler34()} ({time.time()-st} s)')
    
    # THIRTY FIVE:
    st = time.time()
    print(f'Problem 35: {euler35(1000000)} ({time.time()-st} s)')
    
    # THIRTY SIX:
    st = time.time()
    print(f'Problem 36: {euler36(1000000)} ({time.time()-st} s)')
    
    # THIRTY SEVEN (SUPER SLOW!):
    st = time.time()
    #print(f'Problem 37: {euler37(11)} ({time.time()-st} s)')

    # THIRTY EIGHT:
    st = time.time()
    print(f'Problem 38: {euler38()} ({time.time()-st} s)')

    # THIRTY NINE (NOT FAST):
    st = time.time()
    print(f'Problem 39: {euler39(1000)} ({time.time()-st} s)')

    # FORTY:
    st = time.time()
    print(f'Problem 40: {euler40([1,10,100,1000,10000,100000,1000000])} ({time.time()-st} s)')
    
    
