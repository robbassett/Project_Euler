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

# PROJECT EULER 76
def euler76(total):
    coins = np.linspace(1,total,total).astype(int)
    combs = np.zeros((total+1,len(coins)))
    for v in range(combs.shape[0]):
        target = v+1
        for i,c in enumerate(coins):
            if i == 0: combs[v][i] = 1
            elif c <= target:
                combs[v][i] = combs[v][i-1] + combs[target - c - 1][i]
            else:
                combs[v][i] = combs[v][i-1]
    return int(combs[-1][-1]-1)

# PROJECT EULER 77
def euler77(targ):
    ps = primes_lt_n(100)
    v = 2
    while True:
        comb = [1]+[0]*v
        for p in ps:
            for i in range(p,v+1):
                comb[i] += comb[i-p]
        if comb[v] > targ:
            return v
        v+=1

# PROJECT EULER 78
def euler78():
    pn = [1]
    pe = [1]
    s = [1]
    sc = 1
    j = -1
    n = 1
    while True:
        npe = (3*j*j-j)/2
        while npe <= n:
            sc += 1
            s.append(1 if sc <= 2 else -1)
            if sc > 3: sc = 0
            pe.append(int(npe))
            
            if j > 0:
                j *= -1
            else:
                j = (j*-1)+1
                    
            npe = (3*j*j-j)/2
        pn.append(0)
        inds = n-np.array(pe)
        for i,I in enumerate(inds): pn[-1] += int(s[i]*pn[I])
        
        if str(pn[-1])[-6:] == '000000':
            return n
        
        n+=1

# PROJECT EULER 79
def euler79():
    dat = open('aux/e79.dat','r').readlines()
    tries = np.zeros((len(dat),3))
    for i,d in enumerate(dat):
        tries[i] = [int(v) for v in str(d)[:-1]]

    dic = {}
    for n in np.unique(tries):
        dic[n] = set([])
    for t in tries:
        dic[t[1]].add(t[0])
        dic[t[2]].add(t[0])
        dic[t[2]].add(t[1])

    pwd = np.zeros(len(np.unique(tries)))
    for k in dic.keys():
       pwd[len(dic[k])] = k
    out = ''
    for v in pwd:
        out+=str(int(v))
    return out

# PROJECT EULER 80
def euler80():
    def sqrt_100(n,n_decimal=99):
        if np.sqrt(n)%1 == 0:
            return 0
        d = 1
        while d*d <= n:
            d += 1
        root = d-1
        c = (n-root*root)*100
        out = root
        for i in range(n_decimal):
            p = 20*root
            if p > c:
                root*=10
                c*=100
            else:
                st = 1
                while (p+st)*st < c:
                    st += 1
                x = st-1
                root = (root*10)+x
                c -= (p+x)*x
                c *= 100
                out += x
        return out

    ans = 0
    for i in range(2,100):
        ans += sqrt_100(i)
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
    
    # SEVENTY SIX:
    st = time.time()
    print(f'Problem 76: {euler76(100)} ({time.time()-st} s)')
    
    # SEVENTY SEVEN:
    st = time.time()
    print(f'Problem 77: {euler77(5000)} ({time.time()-st} s)')
    
    # SEVENTY EIGHT:
    st = time.time()
    print(f'Problem 78: {euler78()} ({time.time()-st} s)')
    
    # SEVENTY NINE:
    st = time.time()
    print(f'Problem 79: {euler79()} ({time.time()-st} s)')
    
    # EIGHTY:
    st = time.time()
    print(f'Problem 80: {euler80()} ({time.time()-st} s)')
    
    
