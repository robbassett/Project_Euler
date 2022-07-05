from utils import *
import time
import itertools

# PROJECT EULER 91
def euler91(n):
    def get_slope(x,y):
        f = gcf(x,y)
        return y/f,x/f
    
    ans = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            run,rise = get_slope(i,j)
            ans += min([divmod(n-i,run)[0],divmod(j,rise)[0]])*2
    
    return int(ans + 3*n*n)

# PROJECT EULER 92
def euler92():
    def next(v):
        out = 0
        for j in str(v):
            out += int(j)*int(j)
        return out
        
    to_one = set([44])
    to_89 = set([85])
    ans = 0
    for i in range(1,int(1e7)):
        v = i
        ch = [v]
        while True:
            if v in to_one or v == 1:
                for c in ch: to_one.add(c)
                break
            elif v in to_89 or v == 89:
                for c in ch: to_89.add(c)
                ans += 1
                break
            else:
                v = next(v)
                ch.append(v)

    return ans

# PROJECT EULER 93
def euler93():
    def one_op(OP,D1,D2):
        if OP == '+':
            return D1+D2
        if OP == '-':
            return D1-D2
        if op == '/':
            return D1/D2
        return D1*D2
    
    def get_tmv(i,OPS,DS):
        if i == 0:
            tmv = one_op(OPS[0],DS[0],DS[1])
            tmv = one_op(OPS[1],tmv,DS[2])
            return one_op(OPS[2],tmv,DS[3])
            
        if i == 1:
            tmv = one_op(OPS[0],DS[1],DS[2])
            tmv = one_op(OPS[1],DS[0],tmv)
            return one_op(OPS[2],tmv,DS[3])

        if i == 2:
            tmv = one_op(OPS[0],DS[0],DS[1])
            tm2 = one_op(OPS[2],DS[2],DS[3])
            return one_op(OPS[1],tmv,tm2)

        if i == 3:
            tmv = one_op(OPS[1],DS[1],DS[2])
            tmv = one_op(OPS[2],tmv,DS[3])
            return one_op(OPS[0],DS[0],tmv)
                
                
    
    ops = list(itertools.combinations_with_replacement(['+','-','*','/'],3))
    
    digits = list(itertools.combinations([1,2,3,4,5,6,7,8,9],4))
    mx = 0
    for d in digits:
        res = set([])
        for dd in list(itertools.permutations(d)):
            for op in ops:
                for oopp in list(itertools.permutations(op)):
                    for o in range(4):
                        tmv = get_tmv(o,oopp,dd)
                        if tmv > 0 and tmv%1 == 0: res.add(tmv)
                        
                        
        cnt = 0
        ind = 1
        res = sorted(list(res))
        
        while True:
            if res[ind] == res[ind-1]+1:
                pass
            else:
                if res[ind-1] >= mx:
                    ans = np.copy(d)
                    mx = res[ind-1]
                break
            ind += 1

    out = ''
    for v in ans: out+=str(v)
    return out

# PROJECT EULER 94
def euler94():
    s1 = 1
    out = 0
    while True:
        s1 += 1
        if 2*s1 + (s1-1) > 1.e9:
            break
        if np.sqrt(3*s1*s1 + 2*s1 - 1)%1 == 0:
            out += int(2*s1) + int(s1 - 1)
            if s1 < 1000:
                s1*=3
            else:
                s1 = int(s1*3.73)
        elif np.sqrt(3*s1*s1 - 2*s1 -1)%1 == 0:
            out += int(2*s1) + int(s1 + 1)
            if s1 < 1000:
                s1*=3
            else:
                s1 = int(s1*3.73)

    return out

def euler95():
    def next_num(_x):
        return np.array(get_factors(_x)).sum()-_x

    def make_chain(_cv):
        chain = [_cv]
        tv = _cv
        while True:
            tv = next_num(tv)
            if tv in chain or tv > 1.e6:
                chain.append(tv)
                break
            chain.append(tv)
        return chain

    mx = 0
    cv = 219
    while True:
        if cv > 1e6 or mx > 7: break
        cv += 1
        tchain = make_chain(cv)
        if tchain[0] == tchain[-1]:
            if len(tchain) > mx:
                mx = len(tchain)
                ans = min(tchain)
    return ans

def euler96():
    d = open('dat/e96.dat','r').readlines()
    ans = 0
    for i in range(50):
        t=sudoku(d[i*10+1:(i+1)*10],i)
        t.solve()
        tm = ''
        for _ in t.grid[0][:3]: tm+=str(int(_))
        ans+=int(tm)
    return ans

def euler97():
    c = 2
    for i in range(7830456):
        c*=2
        if len(str(c)) > 10:
            c = int(str(c)[-10:])
    ans = c * 28433 + 1
    return str(int(ans))[-10:]

def euler98():
    def check(ws,n):
        wd = {}
        used_nums = []
        for wl,nl in zip(ws[0],str(n)):
            if wl not in wd.keys():
                if nl in used_nums:
                    return False
                wd[wl] = nl
                used_nums.append(nl)
            else:
                if wd[wl] != nl:
                    return False

        cnum = ''
        for wl in ws[1]:
            cnum += wd[wl]
            if cnum == '0':
                return False
        if np.sqrt(float(cnum))%1 == 0:
            return max(n,int(cnum))
        return False

    d = open('dat/e98.dat','r').readline()
    words = np.array([_.replace('"','') for _ in d.split(',')])
    lengths = np.array([len(w) for w in words])
    anagrams = []
    for w,l in zip(words,lengths):
        t = np.where(lengths == l)[0]
        for _w in words[t]:
            if w == _w or [_w,w] in anagrams: continue
            if sorted(w) == sorted(_w):
                anagrams.append([w,_w])

    ps = {}
    i = 1
    while True:
        tm = i*i
        k = len(str(tm))
        if k > 9: break
        if k not in ps:
            ps[k] = [tm]
        else:
            ps[k].append(tm)
        i+=1

    ans = 0
    for a in anagrams:
        for s in ps[len(a[0])]:
            c = check(a,s)
            if c:
                if c > ans:
                    ans  = c
    return ans

def euler99():
    mx = 0
    for i,l in enumerate(open('dat/e99.dat','r').readlines()):
        v1,v2 = [int(_) for _ in l.split(',')]
        tv = v2*np.log10(v1)
        if tv > mx:
            mx = tv
            ans = i+1
    return ans

def euler100():
    b,n = 15,21
    while n < 1.e12:
        b,n = (3*b) + (2*n) - 2,(4*b) + (3*n) - 3
    return b


if __name__ == '__main__':
    # NINTY ONE:
    st = time.time()
    print(f'Problem 91: {euler91(50)} ({time.time()-st} s)')
    
    # NINTY TWO:
    st = time.time()
    print(f'Problem 92: {euler92()} ({time.time()-st} s)')
    
    # NINTY THREE:
    st = time.time()
    print(f'Problem 93: {euler93()} ({time.time()-st} s)')
    
    # NINTY FOUR:
    st = time.time()
    print(f'Problem 94: {euler94()} ({time.time()-st} s)')

    # NINTY FIVE:
    st = time.time()
    print(f'Problem 95: {euler95()} ({time.time()-st} s)')
    
    # NINTY SIX:
    st = time.time()
    print(f'Problem 96: {euler96()} ({time.time()-st} s)')
    
    # NINTY SEVEN:
    st = time.time()
    print(f'Problem 97: {euler97()} ({time.time()-st} s)')

    # NINTY EIGHT:
    st = time.time()
    print(f'Problem 98: {euler98()} ({time.time()-st} s)')
    
    # NINTY NINE:
    st = time.time()
    print(f'Problem 99: {euler99()} ({time.time()-st} s)')

    # ONE HUNDRED:
    st = time.time()
    print(f'Problem 100: {euler100()} ({time.time()-st} s)')