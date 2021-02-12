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

# PROJECT EULER 74
def euler74(N):
    def fact_sum(v):
        return np.array([factorial(int(n)) for n in str(v)]).sum()
    
    def chain_len(v,prev):
        if v in prev.keys():
            return prev[v]
        
        check = [v]
        t = fact_sum(v)
        done = False
        if t == v:
            done = True
        while not done:
            t = fact_sum(t)
            if t in prev.keys():
                cnt = len(check) + prev[t] + 1
                for i,val in enumerate(check[1:]):
                    if val not in prev.keys():
                        prev[val] = prev[t] + len(check) - i - 1
                return cnt
            elif t in check:
                done = True
            else:
                check.append(t)
        prev[v] = len(check)+1
        return len(check)+1

    ans = 0
    prev = {10:3,11:3}
    for i in range(2,N+1):
        if chain_len(i,prev) == 60:
            ans+=1
    return ans

# PROJECT EULER 75
def euler75(mxL):
    def count(m,n,d,mxL=mxL):
        a,b,c = m*m - n*n, 2*m*n, m*m + n*n
        L = a+b+c
        i = 1
        while L*i <= mxL:
            abc = [a*i,b*i,c*i]
            abc.sort()
            if L*i in Ls.keys():
                if abc not in Ls[L*i]: Ls[L*i] += [abc]
            else:
                Ls[L*i]=[abc]
            i+=1
        return L
            
    
    Ls = {}
    n = 0
    done = False
    while not done:
        n+=1
        m = n+1
        L = count(m,n,Ls)
        if L > mxL:
            done = True
        while L <= mxL:
            m+=1
            L = count(m,n,Ls)

    ans = 0
    for k in Ls.keys():
        if k <= mxL and len(Ls[k]) == 1: ans+=1
            
    return ans

if __name__ == '__main__':
    # SEVENTY ONE:
    st = time.time()
    print(f'Problem 71: {euler71(int(1e6))} ({time.time()-st} s)')
    
    # SEVENTY TWO:
    st = time.time()
    print(f'Problem 72: {euler72(int(1e6))} ({time.time()-st} s)')
    
    # SEVENTY THREE:
    st = time.time()
    print(f'Problem 73: {euler73(12000)} ({time.time()-st} s)')
    
    # SEVENTY FOUR (SLOW):
    st = time.time()
    print(f'Problem 74: {euler74(int(1.e6))} ({time.time()-st} s)')
    
    # SEVENTY FIVE:
    st = time.time()
    print(f'Problem 75: {euler75(1500000)} ({time.time()-st} s)')
    
    
