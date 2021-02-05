from utils import *
import time
import itertools

# PROJECT EULER 61
def euler61():
    def gen(a,b,c):
        out = []
        n,v = 1,0
        while v < 10000:
            n+=1
            v = n*(a*n-b)/c
            if v >= 1000:
                out.append(int(v))
                
        return out

    sqrs = gen(1,0,1)
    pents = gen(3,1,2)
    hexs = gen(2,1,1)
    heps = gen(5,3,2)
    octs = gen(3,2,1)

    check = list(itertools.permutations([sqrs,pents,hexs,heps,octs]))
    n = 44
    done = False
    while not done:
        n+=1
        nums = [str(int(n*(n+1)/2))]
        if nums[0][2] != '0':
            for p in check:
                pnums = nums.copy()
                fl = 0
                for ch in p:
                    c1 = pnums[-1][2:]
                    f2 = 1
                    for val in range(11,100):
                        if int(c1+str(val)) in ch and c1+str(val) not in pnums:
                            pnums.append(c1+str(val))
                            f2 = 0
                            break
                    if f2 == 1:
                        fl = 1
                        break
                if fl == 0:
                    if pnums[0][:2] == pnums[-1][2:]:
                        return np.array(pnums).astype(int).sum()

# PROJECT EULER 62:
def euler62(N):
    st = 300
    n = 0
    cubes = []
    vs = []
    while n < N:
        tm=[int(v) for v in str(st**3)]
        tm.sort()
        cubes.append(tm)
        vs.append(st)
        if cubes.count(tm) == N:
            for t,c in enumerate(cubes):
                if c == tm:
                    return vs[t]**3
        st+=1

# PROJECT EULER 63
def euler63():
    count=0
    n=0
    done = False
    while not done:
        l=0
        n+=1
        x=1
        tcnt = 0
        while l <= n:
            l = len(str(x**n))
            if l == n:
                tcnt+=1
            x+=1
        count+=tcnt
        if tcnt == 0:
            done = True
    return count

# PROJECT EULER 64
def euler64(N):
    def get_period_len(v):
        m,d,a0 = [0],[1],int(v**0.5)
        n = 0
        a = [a0]
        p = 0
        while a[-1] != 2*a0:
            p+=1
            m.append(d[n]*a[n]-m[n])
            d.append((v-m[-1]*m[n+1])/d[n])
            a.append(int((a0+m[n+1])/d[n+1]))
            n+=1
        return a,p

    count = 0
    for i in range(1,N+1):
        if np.sqrt(i)%1 != 0:
            a,p = get_period_len(i)
            if p%2 != 0: count+=1
    return count

# PROJECT EULER 65
def euler65(N):
    N-=1
    l = []
    n = 1
    while len(l) < N:
        l += [1,2*n,1]
        n+=1
    l = l[:N][::-1]

    n,d = 1,l[0]
    for i in range(1,N):
        n += d*l[i]
        n,d = d,n
    n += 2*d
    ans = 0
    for v in str(n): ans+=int(v)
    return ans

# PROJECT EULER 66
def euler66(N):
    def get_conv_frac(a):
        l = a[::-1]
        n,d = 1,l[0]
        for i in range(1,len(l)-1):
            n += d*l[i]
            n,d = d,n
        n += l[-1]*d
        return n,d
    
    def solve(v):
        m,d,a0 = [0],[1],int(v**0.5)
        n = 0
        a = [a0]
        p = 0
        solved = False
        while not solved:
            p+=1
            m.append(d[n]*a[n]-m[n])
            d.append((v-m[-1]*m[n+1])/d[n])
            a.append(int((a0+m[n+1])/d[n+1]))
            h,k = get_conv_frac(a)
            if (h*h)-(v*k*k) == 1:
                solved = True
                
            n+=1
        return h,k

    mx = 0
    ans = 0
    for D in range(1,N+1):
        if np.sqrt(D)%1 != 0:
            x,y = solve(D)
            if x > mx:
                mx = x
                ans = D

    return ans

if __name__ == '__main__':
    # SIXTY ONE:
    st = time.time()
    print(f'Problem 61: {euler61()} ({time.time()-st} s)')
    
    # SIXTY TWO:
    st = time.time()
    print(f'Problem 62: {euler62(5)} ({time.time()-st} s)')
    
    # SIXTY THREE:
    st = time.time()
    print(f'Problem 63: {euler63()} ({time.time()-st} s)')
    
    # SIXTY FOUR:
    st = time.time()
    print(f'Problem 64: {euler64(10000)} ({time.time()-st} s)')
    
    # SIXTY FIVE:
    st = time.time()
    print(f'Problem 65: {euler65(100)} ({time.time()-st} s)')
    
    # SIXTY SIX:
    st = time.time()
    print(f'Problem 66: {euler66(1000)} ({time.time()-st} s)')

    # SIXTY SEVEN SOLVED PREVIOUSLY!

    
