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

        


if __name__ == '__main__':
    # NINTY ONE:
    st = time.time()
    #print(f'Problem 91: {euler91(50)} ({time.time()-st} s)')
    
    # NINTY TWO:
    st = time.time()
    #print(f'Problem 92: {euler92()} ({time.time()-st} s)')
    
    # NINTY THREE:
    st = time.time()
    #print(f'Problem 93: {euler93()} ({time.time()-st} s)')
    
    # NINTY FOUR:
    st = time.time()
    #print(f'Problem 94: {euler94()} ({time.time()-st} s)')

    # NINTY FIVE:
    st = time.time()
    print(f'Problem 95: {euler95()} ({time.time()-st} s)')