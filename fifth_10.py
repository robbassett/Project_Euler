from utils import *
import time

# PROJECT EULER 41:
def euler41():
    ps = primes_lt_n(10000000)
    o = 0
    for digits in [4,5,6,7]:
        t = np.where((ps > 10**(digits-1)-1)&(ps < 10**digits))[0]
        for p in ps[t]:
            s = str(p)
            fl = 1
            for i in range(1,digits+1):
                if s.count(str(i)) != 1:
                    fl = 0
                    break
            if fl == 1:
                o=p
    return o

# PROJECT EULER 42:
def euler42():
    tris = [1]
    ind = 2
    while max(tris) < 300:
        tris.append(0.5*ind*(ind+1))
        ind+=1
    c=0
    l = open('aux/e42.dat','r').readline().split(',')
    l[-1] = l[-1][:-1]
    words = [i[1:-1] for i in l]
    for w in words:
        if sum([char_position(l) for l in w]) in tris: c+=1
        
    return c

# PROJECT EULER 43:
def euler43():
    def check(l):
        fl = 0
        vs = [2,3,5,7,11,13,17]
        for i in range(2,9):
            tm = ''
            for j in range(i-1,i+2): tm+=str(l[j])
            if int(tm)%vs[i-2] != 0:
                fl = 1
                break
        if fl == 0:
            return True
        else:
            return False
    
    pdn = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))
    o = 0
    for pd in pdn:
        if check(pd):
            tm = ''
            for v in pd: tm+=str(v)
            o+=int(tm)
    return o

# PROJECT EULER 44:
def euler44():
    pd = np.array([i*(3*i-1)/2 for i in range(1,7000)])
    for p in pd:
        t = pd+p
        z = np.intersect1d(t,pd)
        if len(z) > 0:
            for f in z:
                i = list(pd).index(f)
                if np.sqrt(1+24*(pd[i]+p))%1 == 0:
                    o = int(abs(p-pd[i]))
    return o

# PROJECT EULER 45:
def euler45(n_start):
    done = False
    n = n_start
    while not done:
        T = n*(n+1)/2
        if ((1.+np.sqrt(1.+24*T))/6)%1 == 0:
            if ((1.+np.sqrt(1+8*T))/4.)%1 == 0:
                o = n
                break
            else:
                n+=1
        else:
            n+=1
    return int(o*(o+1)/2)

# PROJECT EULER 46:
def euler46():
    mx_guess = 10000
    ps = primes_lt_n(mx_guess)
    ocomps = np.setdiff1d(np.arange(9,mx_guess,2),ps)
    for v in ocomps:
        f = 1
        for p in ps:
            if p > v:
                break
            d = (v-p)/2
            if np.sqrt(d)%1 == 0:
                f = 0
                break
        if f == 1:
            return v

if __name__ == '__main__':
    # FORTY ONE:
    st = time.time()
    print(f'Problem 41: {euler41()} ({time.time()-st} s)')
    
    # FORTY TWO:
    st = time.time()
    print(f'Problem 42: {euler42()} ({time.time()-st} s)')
    
    # FORTY THREE:
    st = time.time()
    print(f'Problem 43: {euler43()} ({time.time()-st} s)')
    
    # FORTY FOUR:
    st = time.time()
    print(f'Problem 44: {euler44()} ({time.time()-st} s)')
    
    # FORTY FIVE:
    st = time.time()
    print(f'Problem 45: {euler45(286)} ({time.time()-st} s)')
    
    # FORTY SIX:
    st = time.time()
    print(f'Problem 46: {euler46()} ({time.time()-st} s)')
