from utils import *
import time

# PROJECT EULER 51:
def euler51(n):
    mx_guess = int(1.e7)
    ps = primes_lt_n(mx_guess)
    ps = ps[np.where(ps > 100000)[0]]
    to_check = [str(v) for v in range(10-n)]
    ans = -1
    for p in ps:
        chs = []
        for c in to_check:
            if str(p).count(c) != 0:
                chs.append(c)
        if len(chs) > 0:
            for cc in chs:
                t=np.array([v for v in str(p)])
                d = np.where(t == cc)[0]
                c = 0
                for i in range(10):
                    if str(i) != cc:
                        l = np.copy(t)
                        l[d] = i
                        f = ''
                        for v in l: f+=v
                        if int(f) in ps: c+=1
                    if c == n:
                        ans = p
                        break
                if ans != -1:
                    break
        if ans != -1:
            break
    return ans

# PROJECT EULER 52:
def euler52():
    n = 1
    done = False
    while not done:
        n+=1
        if len(str(n)) == len(str(n*6)):
            ch = [int(v) for v in str(n)]
            ch.sort()
            fl = 0
            for i in range(2,7):
                tm = [int(v) for v in str(n*i)]
                tm.sort()
                if tm != ch:
                    fl = 1
                    break
            if fl == 0:
                ans = n
                done = True
    return n

# PROJECT EULER 53:
def euler53():
    c = 0
    for n in range(0,101):
        for r in range(0,n+1):
            f1,f2,f3 = factorial(n),factorial(r),factorial(n-r)
            if f1/(f2*f3) > 1.e6:
                c+=1
    return c

# PROJECT EULER 54:
def euler54():
    ndic = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    sdic = ['S','D','H','C']
    def parse_hand(h):
        out = np.zeros((2,5))
        for i,c in enumerate(h):
            out[0][i] = ndic.index(c[0])
            out[1][i] = sdic.index(c[1])
        return out

    def rank_hand(h):
        parsed = parse_hand(h)
        cnts = np.zeros(13)
        for v in range(13):
            cnts[v] = list(parsed[0]).count(v)
        if 4 in cnts:
            return [7,np.where(cnts == 4)[0]]
        if 3 in cnts:
            if 2 in cnts:
                return [6,np.where(cnts == 3)[0][0]]
            else:
                return [3,np.where(cnts == 3)[0][0]]
        if 2 in cnts:
            if list(cnts).count(2) == 2:
                return [2,max(np.where(cnts == 2)[0])]
            else:
                return [1,np.where(cnts == 2)[0][0]]

        straight = True
        flush = False
        royal = False
        ch = np.copy(parsed[0])
        ch.sort()
        sf = 0
        for i in range(len(ch)-1):
            if ch[i+1] != ch[i]+1:
                straight = False
                break
            
        if straight:
            if min(ch) == 8:
                royal = True
                
        if list(parsed[1]).count(parsed[1][0]) == len(parsed[1]):
            flush = True

        if flush and not straight:
            return [5,max(parsed[0])]
        if straight and not flush:
            return [4,max(parsed[0])]
        if flush and straight and not royal:
            return [8,max(parsed[0])]
        if flush and royal:
            return [9,max(parsed[0])]

        return [0,max(parsed[0])]
        
    
    hands = open('dat/e54.dat').readlines()
    wins = np.zeros(len(hands))
    for i,l in enumerate(hands):
        h1,h2 = l.split()[:5],l.split()[5:]
        r1 = rank_hand(h1)
        r2 = rank_hand(h2)
        if r1[0] > r2[0]:
            wins[i] = 1
        elif r2[0] > r1[0]:
            wins[i] = 2
        elif r2[0] == r1[0]:
            if r1[1] > r2[1]:
                wins[i] = 1
            elif r2[1] > r1[1]:
                wins[i] = 2

    return list(wins).count(1)

# PROJECT EULER 55:
def euler55():
    l_count = 0
    for i in range(1,10001):
        fl = 0
        n1 = i
        for j in range(50):
            n1 += int(str(n1)[::-1])
            if str(n1) == str(n1)[::-1]:
                fl = 1
                break
        if fl == 0:
            l_count+=1

    return l_count

# PROJECT EULER 56:
def euler56():
    mx_sum = 0
    for a in range(1,100):
        for b in range(1,100):
            t = a**b
            s = 0
            for v in str(t): s+=int(v)
            if s > mx_sum:
                mx_sum = s

    return mx_sum

# PROJECT EULER 57:
def euler57():
    i = 2
    ln,ld = 1,2
    count = 0
    for j in range(1000):
        bn,bd = ld,(2*ld)+ln
        if len(str(bd+bn)) > len(str(bd)): count+=1 
        ln,ld = bn,bd
    return count

# PROJECT EULER 58:
def euler58(target):
    cnt = 1
    pcnt = 0
    cv = 1
    ext = 2
    curr = 100
    while curr > target:
        cnt+=4
        for i in range(4):
            if is_prime(cv+(i+1)*ext): pcnt+=1
        cv += 4*ext
        curr = pcnt/cnt
        sl = ext+1
        ext+=2

    return sl

# PROJECT EULER 59:
def euler59():
    b = open('dat/e59.dat','r').readline().split(',')
    b[-1] = b[-1][:-1]
    ords = [ord(v) for v in ['e','a','r','i','o','t','n','s']]
    pk = np.arange(97,123,1).astype(int)
    l1,l2,l3 = [],[],[]
    for i,v in enumerate(b):
        if i%3 == 0:
            l1.append(int(v))
        elif i%3 == 1:
            l2.append(int(v))
        else:
            l3.append(int(v))
            
    key = ['0','0','0']
    for i,l in enumerate([l1,l2,l3]):
        freqs = np.zeros(pk.shape)
        for j,p in enumerate(pk):
            c = 0
            for v in l:
                if v^p in ords: c+=1
            freqs[j] = c
        key[i] = pk[np.argmax(freqs)]

    out = 0
    for i,v in enumerate(b):
        out += int(v)^key[i%3]
    return out

# PROJECT EULER 60:
def euler60():
    def check(v1,v2):
        if is_prime(int(str(v1)+str(v2))) and is_prime(int(str(v2)+str(v1))):
            return True
        else:
            return False
    
    mx_guess = 10000
    ps = primes_lt_n(mx_guess)
    for i,a in enumerate(ps):
        for j,b in enumerate(ps[i+1:]):
            if check(a,b):
                for k,c in enumerate(ps[j+1:]):
                    if check(a,c) and check(b,c):
                        for l,d in enumerate(ps[k+1:]):
                            if check(a,d) and check(b,d) and check(c,d):
                                for m,e in enumerate(ps[l+1:]):
                                    if check(a,e) and check(b,e) and check(c,e) and check(d,e):
                                        return sum([a,b,c,d,e])

if __name__ == '__main__':
    # FIFTY ONE:
    st = time.time()
    print(f'Problem 51: {euler51(7)} ({time.time()-st} s)')
    
    # FIFTY TWO:
    st = time.time()
    print(f'Problem 52: {euler52()} ({time.time()-st} s)')
    
    # FIFTY THREE:
    st = time.time()
    print(f'Problem 53: {euler53()} ({time.time()-st} s)')
    
    # FIFTY FOUR:
    st = time.time()
    print(f'Problem 54: {euler54()} ({time.time()-st} s)')
    
    # FIFTY FIVE:
    st = time.time()
    print(f'Problem 55: {euler55()} ({time.time()-st} s)')
    
    # FIFTY SIX:
    st = time.time()
    print(f'Problem 56: {euler56()} ({time.time()-st} s)')
    
    # FIFTY SEVEN:
    st = time.time()
    print(f'Problem 57: {euler57()} ({time.time()-st} s)')
    
    # FIFTY EIGHT:
    st = time.time()
    print(f'Problem 58: {euler58(0.1)} ({time.time()-st} s)')
    
    # FIFTY NINE:
    st = time.time()
    print(f'Problem 59: {euler59()} ({time.time()-st} s)')
    
    # SIXTY:
    st = time.time()
    print(f'Problem 60: {euler60()} ({time.time()-st} s)')
