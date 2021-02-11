from utils import *
import time
import itertools

# PROJECT EULER 71
def euler71(d):
    fracs = []
    vals = []
    for d in range(2,d+1):
        n = int(d*(3/7))
        if n/d < 3/7:
            fracs.append(f'{n}/{d}')
            vals.append(n/d)
    indices = np.argsort(vals)
    return fracs[indices[-1]].split('/')[0]

# PROJECT EULER 72
def euler72(n):
    ans = 0
    phi = np.arange(0,n+1)
    for i in range(2,n+1):
        if i == phi[i]:
            for j in range(i,n+1,i):
                phi[j] *= (1-(1./i))
        ans+=phi[i]
    return ans

# PROJECT EULER 73
def euler73(n):
    cnt = 0
    for d in range(2,n+1):
        lo,hi = int(d/3),int(d/2)+1
        for v in range(lo,hi):
            if v/d > 1/3 and v/d < 1/2:
                if np.gcd(v,d) == 1:
                    cnt+=1
    return cnt

if __name__ == '__main__':
    # SEVENTY ONE:
    st = time.time()
    print(f'Problem 71: {euler71(int(1e6))} ({time.time()-st} s)')
    
    # SEVENTY TWO:
    st = time.time()
    print(f'Problem 72: {euler72(int(1e6))} ({time.time()-st} s)')
    
    # SEVENTY THREE:
    st = time.time()
    print(f'Problem 73: {euler73(int(12000))} ({time.time()-st} s)')
    
    
