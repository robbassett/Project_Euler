from utils import *
import time
import itertools

# PROJECT EULER 81
def euler81():
    d = open('aux/e81.dat','r').readlines()
    m = np.zeros((len(d),len(d)))
    for i in range(len(d)):
        m[i] = np.array(d[i].split(',')).astype(int)

    min_sum = np.zeros(m.shape)
    min_sum[0,0] = m[0,0]
    for i in range(1,m.shape[0]):
        min_sum[0,i] = m[0,i] + min_sum[0,i-1]
        min_sum[i,0] = m[i,0] + min_sum[i-1,0]

    for i in range(1,m.shape[0]):
        min_sum[i,i] = m[i,i] + min([min_sum[i-1,i],min_sum[i,i-1]])
        for j in range(i+1,m.shape[0]):
            min_sum[i,j] = m[i,j] + min([min_sum[i,j-1],min_sum[i-1,j]])
            min_sum[j,i] = m[j,i] + min([min_sum[j,i-1],min_sum[j-1,i]])
        
    return int(min_sum[-1,-1])

# PROJECT EULER 82
def euler82():
    
    d = open('aux/e81.dat','r').readlines()
    m = np.zeros((len(d),len(d)))
    for i in range(len(d)):
        m[i] = np.array(d[i].split(',')).astype(int)
        
    min_sum = np.zeros((m.shape[0],*m.shape))
    min_sum[:,:,0] = m[:,0]
    for k in range(m.shape[0]-1):
        for v in range(m.shape[0]):
            min_sum[v,v,k+1] = min_sum[v,v,k] + m[v,k+1]
            for i in range(v-1,-1,-1): min_sum[v,i,k+1] = min_sum[v,i+1,k+1] + m[i,k+1]
            for i in range(v+1,m.shape[0]): min_sum[v,i,k+1] = min_sum[v,i-1,k+1] + m[i,k+1]

        col_min = min_sum.min(axis=0)
        for v in range(m.shape[0]): min_sum[v] = np.copy(col_min)

    min_sum = min_sum.min(axis=0)
    return int(min_sum[:,-1].min())

# PROJECT EULER 83
def euler83():
    d = open('aux/e81.dat','r').readlines()
    m = np.zeros((len(d),len(d)))
    for i in range(len(d)):
        m[i] = np.array(d[i].split(',')).astype(int)

    v = np.zeros(m.shape) + np.nan
    g = np.empty(m.shape) + 1.e40
    g[0,0] = m[0,0]
    current_node = (0,0)
    mxr,mxc = 0,0
    op = [current_node]
    while len(op) != 0:
        for ij in [(-1,0),(1,0),(0,-1),(0,1)]:
            check_node = (current_node[0]+ij[0],current_node[1]+ij[1])
            if check_node[0] >= 0 and check_node[1] >= 0 and check_node[0] < m.shape[0] and check_node[1] < m.shape[0]:
                if g[check_node] > m[check_node]+g[current_node]:
                    g[check_node] = m[check_node]+g[current_node]
                    if check_node not in op:
                        v[check_node] = np.nan
                        op.append(check_node)
        op.remove(current_node)
        v[current_node] = 1.0

        if len(op) == 0:
            break
        
        vals = np.zeros(len(op))
        for i,c in enumerate(op):
            vals[i] = g[c]
            if c[0] > mxr: mxr = c[0]
            if c[1] > mxc: mxc = c[1]

        current_node = op[np.argmin(vals)]

    return int(g[-1,-1])

# PROJECT EULER 84
def euler84(n_side):
    
    def roll():
        vals = np.random.randint(1,n_side+1,2)
        doub = True if vals[0] == vals[1] else False
    
        return vals.sum().astype(int),doub

    def CC(ccn,cc_stack):
        i = ccn%16
        if cc_stack[i] == 0:
            return 0
        if cc_stack[i] == 1:
            return 10
        return -1

    def CH(sp,chn,ch_stack):
        i = chn%16
        if ch_stack[i] == 0:
            return 0
        if ch_stack[i] == 1:
            return 10
        if ch_stack[i] == 2:
            return 11
        if ch_stack[i] == 3:
            return 24
        if ch_stack[i] == 4:
            return 39
        if ch_stack[i] == 5:
            return 5
        if ch_stack[i] in [6,7]:
            if sp == 7:
                return 15
            if sp == 22:
                return 25
            if sp == 36:
                return 5
        if ch_stack[i] == 8:
            if sp in [7,36]:
                return 12
            if sp == 22:
                return 28
        if ch_stack[i] == 9:
            return sp - 3
        return -1

    cc_stack = np.linspace(0,16,16).astype(int)
    np.random.shuffle(cc_stack)
    ccn = 0
    
    ch_stack = np.linspace(0,16,16).astype(int)
    np.random.shuffle(ch_stack)
    chn = 0
    
    counts = np.zeros(40)
    nrolls = 500000
    sp = 0
    dcount = 0
    for _ in range(nrolls):
        r,d = roll()
        if d:
            dcount += 1
        else:
            dcount = 0

        if dcount == 3:
            sp = 10
            
        else:
            sp += r
            if sp in [2,17,33]:
                t = CC(ccn,cc_stack)
                ccn+=1
                if t != -1: sp = t
            if sp in [7,22,36]:
                t = CH(sp,chn,ch_stack)
                chn+=1
                if t != -1: sp = t
        
        if sp == 30:
            sp = 10
        
        if sp > 39:
            sp -= 40
        
        counts[int(sp)] += 1
    
    probs = counts/nrolls
    ans = np.argsort(probs)[::-1][:3]
    out = ''
    for a in ans: out+=str(a)
    return out

# PROJECT EULER 85
def euler85():
    def Nrec(H,W):
        n = 0
        for i in range(H):
            for j in range(W): n+=(H-i)*(W-j)
        return n
    
    W = 100
    x,y = [],[]
    for w in range(1,W):
        for h in range(1,w-1):
            if abs(Nrec(h,w)-2.e6) < 50:
                return int(h*w)

# PROJECT EULER 86
def euler86(targ):
    count = 0
    l = 1
    while True:
        for o in range(1,2*l):
            if np.sqrt(o*o + l*l)%1 == 0:
                if o <= l:
                    count += int(o/2)
                else:
                    count += 1+l-o/2
        l+=1
        if count >= targ:
            break
    return l

# PROJECT EULER 87
def euler87(targ):
    ps = primes_lt_n(10000)
    i,j,k = 0,0,0
    nums = []
    while True:
        a = ps[i]
        v1 = a*a
        if v1+np.power(ps[0],3)+np.power(ps[0],4) > targ:
            break
        while True:
           b = ps[j]
           v2 = b*b*b
           if v1+v2+np.power(ps[0],4) > targ:
               j = 0
               break
           while True:
               c = ps[k]
               v3 = c*c*c*c
               if v1+v2+v3 > targ:
                   k = 0
                   break
               nums.append(v1+v2+v3)
               k+=1
           j+=1
        i+=1
    return len(set(nums))

if __name__ == '__main__':
    # EIGHTY ONE:
    st = time.time()
    print(f'Problem 81: {euler81()} ({time.time()-st} s)')
    
    # EIGHTY TWO:
    st = time.time()
    print(f'Problem 82: {euler82()} ({time.time()-st} s)')

    # EIGHTY THREE (Dijkstra's Algorithm):
    st = time.time()
    print(f'Problem 83: {euler83()} ({time.time()-st} s)')

    # EIGHTY FOUR (MC sim):
    st = time.time()
    print(f'Problem 84: {euler84(4)} ({time.time()-st} s)')

    # EIGHTY FIVE:
    st = time.time()
    print(f'Problem 85: {euler85()} ({time.time()-st} s)')

    # EIGHTY SIX:
    st = time.time()
    print(f'Problem 86: {euler86(1e6)} ({time.time()-st} s)')

    # EIGHTY SEVEN:
    st = time.time()
    print(f'Problem 87: {euler87(5e7)} ({time.time()-st} s)')
    
