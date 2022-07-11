import numpy as np
import utils
import time

def get_possibles(seq,i=0,opts=[],mxrng=3):
    used = [a+b for a,b in zip(seq,opts)]
    out,new = [],[]
    rng = (-mxrng,mxrng)
    for r in range(rng[0],rng[1]+1):
        if seq[i]+r in used or seq[i]+r <= 0: continue
        out.append(r)

        if i < len(seq)-1:
            tm,tn = get_possibles(seq,i+1,opts+[r])
            if i < len(seq)-2:
                new += tn
            else:
                t1 = opts+[r]
                for v in tm:
                    topts = t1 + [v]
                    vals = [a+b for a,b in zip(topts,seq)]
                    new.append(vals)

    return out,new

def euler101(k):
    def lagrange(x,y):
        p = np.poly1d(0)
        for i in range(len(x)):
            pt = np.poly1d(y[i])
            for j in range(len(x)):
                if j == i: continue
                pt *= np.poly1d([1,-x[j]])/(x[i]-x[j])
            p = np.poly1d(0)+pt if i == 0 else p+pt
        return p.coef

    def func(n,d=10):
        out = 1
        for _ in range(1,d+1):
            t = 1
            for _v in range(_):
               t = t*n
            if _%2 != 0: t*= -1
            out += t
        return out

    def pred(n,p):
        out = np.zeros(len(n))
        for i,_p in enumerate(p):
            out += _p*np.power(n,len(p)-i-1)
        return out

    ans = [1]
    x,y = [1],[1]
    for i in range(k-1):
        tx,ty = i+2,func(i+2)
        x.append(tx)
        y.append(ty)
        ans.append(round(pred(np.linspace(0,max(x)+1,100),lagrange(x,y))[-1]))
    return sum(ans)

def euler102():
    def check(A,B,C):
        axes = set()
        for _x in [A,B,C]:
            for _y in [A,B,C]:
                if _x == _y: continue
                if _y[0] == _x[0]:
                    y0 = 1.e6
                    x0 = _x[0]
                elif _y[1] == _x[1]:
                    x0 = 1.e6
                    y0 = _x[1]
                else:
                    m = (_y[1]-_x[1])/(_y[0]-_x[0])
                    y0 = _x[1] - m*_x[0]     
                    x0 = -y0/m
                if (_x[0] < x0 and x0 < _y[0]) or (_x[0] > x0 and x0 > _y[0]):
                    ts = 0 if x0 > 0 else 2
                    axes.add(ts)
                if (_x[1] < y0 and y0 < _y[1]) or (_x[1] > y0 and y0 > _y[1]):
                    ts = 1 if y0 > 0 else 3
                    axes.add(ts)

        if x0 == 1.e6:
            return True

        if len(axes) == 4:
            return True
        return False    

    ans = 0
    for l in open('dat/e102.dat','r').readlines():
        x = l.split(',')
        if check(
            (float(x[0]),float(x[1])),
            (float(x[2]),float(x[3])),
            (float(x[4]),float(x[5]))
        ):
            ans += 1
    return ans
 
def euler103(n=7):
    def check_special(s):
        if len(s) < 3: return True
        for n in range(2,len(s)):
            for _x in utils.itertools.permutations(s,n):
                _z = set(s).difference(set(_x))
                if sum(_x) in _z: 
                    return False
                for _n in range(1,len(_z)+1):
                    for _y in utils.itertools.permutations(_z,_n):
                        SB,SC = [sum(_x),sum(_y)] if len(_x) > len(_y) else [sum(_y),sum(_x)]
                        sbc = SB < SC if len(_x) != len(_y) else False
                        if sum(_x) == sum(_y) or sbc:
                            return False
        return True

    ts = [1,2]
    for _n in range(3,n+1):
        b = ts[int(np.floor(len(ts)/2))]
        S = [b] + [_+b for _ in ts]
        # Turns out the near optimum estimate from the optimum for n=6 is also optimum!
        # no need to explore for n=7
        if len(S) == 6:
            for _c in utils.itertools.combinations_with_replacement([-2,-1,0,1,2],len(S)):
                if list(_c).count(-3) > 1: continue
                if sum(_c) >= 0: continue
                for _ in set(utils.itertools.permutations(_c)):
                    tS = np.array(S)+_
                    if len(set(tS)) < len(S): continue
                    if any([_ <= 0 for _ in tS]): continue
                    if check_special(tS):
                        if sum(tS) < sum(S):
                            S = sorted(tS)
                            break
        ts = S
    
    ans = ''
    for s in ts: ans+=str(s)
    return ans

def euler103b(n=7):
    def check_special1(s):
        if len(s) < 3: return True
        for n in range(2,len(s)):
            for _x in utils.itertools.combinations(s,n):
                _z = set(s).difference(set(_x))
                if sum(_x) in _z: 
                    return False
                for _n in range(1,n+1):
                    for _y in utils.itertools.combinations(_z,_n):
                        SB,SC = sum(_x),sum(_y)
                        sbc = SB > SC if len(_x) != len(_y) else False
                        if SB == SC or sbc:
                            return False
        return True

    def check_special(s):
        if len(s) < 3: return True
        for n in range(1,len(s)):
            for _x in utils.itertools.combinations(s,n):
                _z = set(s).difference(set(_x))
                if sum(_x) in _z: 
                    return False
                for _n in range(n,n+2):
                    for _y in utils.itertools.combinations(_z,_n):
                        SB,SC = sum(_x),sum(_y)
                        sbc = SB > SC if len(_x) != len(_y) else False
                        if SB == SC or sbc:
                            return False
        return True

    print(check_special([1,2,4,8]))

    ts = [2,3,4]
    for _N in range(4,n+1):
        b = ts[int(np.floor(len(ts)/2))]
        S = [b] + [_+b for _ in ts]
        _,possibles = get_possibles(S)
        for c in possibles:
            f = True
            if check_special(c) and sum(c) < sum(S):
                ts = c
                f = False
                break
        if f:
            ts = S
    
        print(_N,ts)

    ans = ''
    for s in ts: ans+=str(s)
    return ans

def euler104():
    def check(fn,ln):
        if len(set(sorted(str(fn)[:9])).difference({'0'})) == 9:
            if len(set(sorted(str(ln)[:9])).difference({'0'})) == 9:
                return True
        return False

    fp,fv = 1,1
    sp,sv = 1,1
    N = 2
    done = False
    while True:
        N += 1
        _v = sp+sv
        sp,sv = int(sv%1.e9),int(_v%1.e9)
        _v = fp+fv
        if _v > 1.e15:
            _v = int(str(_v)[:15])
            fv/=10
        fp,fv = fv,_v
        if check(fv,sv):
            return N

def euler105():
    def check_special(s):
        if len(s) < 3: return True
        for n in range(2,len(s)//2+1):
            for _x in utils.itertools.combinations(s,n):
                _z = set(s).difference(set(_x))
                if sum(_x) in _z: 
                    print(len(s),_x,_z,n)
                    return False
                for _n in range(n,n+2):
                    for _y in utils.itertools.combinations(_z,_n):
                        SB,SC = sum(_x),sum(_y)
                        sbc = SB > SC if len(_x) != len(_y) else False
                        if SB == SC or sbc:
                            
                            print(len(s),_x,_y,SB,SC)
                            return False
        return True

    ans = 0
    for l in open('dat/e105.dat','r').readlines():
        x = [int(_) for _ in l.split(',')]
        if check_special(x):
            ans+=sum(x)
        print(x,ans)
    return ans

test = [1219,1183,1182,1115,1035,1186,591,1197,1167,887,1184,1175]
t1 = [81,88,75,42,87,84,86,65]
t2 = [157,150,164,119,79,159,161,139,158]

if __name__ == '__main__':
    # ONE HUNDRED AND ONE:
    st = time.time()
    print(f'Problem 101: {euler101(10)} ({time.time()-st} s)')

    # ONE HUNDRED AND TWO:
    st = time.time()
    print(f'Problem 102: {euler102()} ({time.time()-st} s)')
    
    # ONE HUNDRED AND THREE:
    st = time.time()
    print(f'Problem 103: {euler103()} ({time.time()-st} s)')

    # ONE HUNDRED AND FOUR:
    st = time.time()
    print(f'Problem 104: {euler103()} ({time.time()-st} s)')