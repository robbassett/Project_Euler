import numpy as np
import utils
import time

def check_special(s):
        if len(s) < 3: return True
        for n in range(2,len(s)):
            for _x in utils.itertools.permutations(s,n):
                _y = set(s).difference(set(_x))
                SB,SC = [sum(_x),sum(_y)] if len(_x) > len(_y) else [sum(_y),sum(_x)]
                sbc = SB < SC if len(_x) != len(_y) else False
                print(_x,_y)
                print(SB,SC)
                print(sbc)

                if sum(_x) == sum(_y) or sbc:
                    #print(_x,_y,SB,SC)
                    return False
        return True

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
 
def euler103():
    n=7
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
                            if len(s) == 600:
                                print(_x,_y,SB,SC)
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