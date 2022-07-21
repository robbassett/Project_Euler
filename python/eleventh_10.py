import numpy as np
import utils
import time
import copy

def euler101(k=10):
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
    def get_possibles(seq,i=0,opts=[],mxrng=3):
        used = [a+b for a,b in zip(seq,opts)]
        out,new = [],[]
        rtop = mxrng if sum(opts) < -mxrng else abs(sum(opts)+1)
        rng = (-mxrng,rtop)
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
                        if sum(topts) < 0:
                            new.append(vals)

        return out,new

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
                    return False
                for _n in range(n,n+2):
                    for _y in utils.itertools.combinations(_z,_n):
                        SB,SC = sum(_x),sum(_y)
                        sbc = SB > SC if len(_x) != len(_y) else False
                        if SB == SC or sbc:
                            return False
        return True

    ans = 0
    for l in open('dat/e105.dat','r').readlines():
        x = [int(_) for _ in l.split(',')]
        if check_special(x):
            ans+=sum(x)
    return ans

def euler106(n=7):
    def get_subset_pairs(s):
        spairs = []
        count = 0
        for n in range(2,len(s)//2+1):
            for _x in utils.itertools.combinations(s,n):
                _z = set(s).difference(set(_x))
                for _y in utils.itertools.combinations(_z,n):
                    if [_y,_x] not in spairs: 
                        spairs.append([_x,_y])
                        if not all([i < j for i,j in zip(_x,_y)]):
                            count+=1
        return count

    return get_subset_pairs(np.linspace(1,n,n).astype(int))

def euler107():
    first = True
    for line in open('dat/e107.dat','r').readlines():
        row = np.array(line.replace('-','0').replace('\n','').split(',')).astype(float)
        if first:
            first=False
            mat = row
        else:
            mat = np.vstack((mat,row))

    # Solved with Prim's algorithm
    F = [0]
    ans = 0
    while True:
        mn = 1000
        for i in F:
            for j in range(len(mat)):
                if mat[i,j] == 0 or j in F: continue
                if mat[i,j] < mn:
                    mn = mat[i,j]
                    _i,_j = i,j
        F.append(_j)
        ans+=mn
        if len(F) == len(mat): break

    return int(mat.sum()/2)-int(ans)

def euler108():
    def f(x,n):
        return x*n/(x-n)

    _mx,_my = [],[]
    mc = 0
    n = 1
    dn = 1
    while True:
        count = 0
        x = n+1
        while True:
            y = f(x,n)
            if abs(round(y)-y) < 1.e-10:
                count += 1
            x+=1
            if y < 2*n: break

        if count > 1000:
            break

        if count > mc:
            mc = count
            _mx.append(n)
            _my.append(count)
        if len(_mx) > 36:
            break
        if len(_mx) > 3:
            dn = 6
        if len(_mx) > 6:
            dn = 30
        if len(_mx) > 13:
            dn = 420
        if len(_mx) > 20:
            dn = 4620

        n+=dn
    return n
    
def euler109():
    scores = np.linspace(1,20,20).astype(int)
    scores = np.concatenate((scores,[25]))
    doubles = scores*2
    all_vals = [str(_)+'S' for _ in scores] + [str(_)+'D' for _ in scores] + [str(_)+'T' for _ in scores[:-1]]

    md = {'S':1,'D':2,'T':3}
    cd = {}
    for val in list(doubles):
        cd[val] = 1

    for comb in utils.itertools.combinations_with_replacement(all_vals,2):
        if not any (['D' in _ for _ in comb]): continue
        V = int(comb[0][:-1])*md[comb[0][-1]]+int(comb[1][:-1])*md[comb[1][-1]]
        if V > 99: continue
        if V not in cd.keys():
            cd[V] = 1
        else:
            cd[V] += 1
        if all(['D' in _ for _ in comb]) and comb[0] != comb[1]:
            cd[V] += 1

    for comb in utils.itertools.combinations_with_replacement(all_vals,3):
        if not any (['D' in _ for _ in comb]): continue
        V = int(comb[0][:-1])*md[comb[0][-1]]+int(comb[1][:-1])*md[comb[1][-1]]+int(comb[2][:-1])*md[comb[2][-1]]
        ds = [_ for _ in comb if 'D' in _]
        if V > 99: continue
        if V not in cd.keys():
            cd[V] = len(set(ds))
        else:
            cd[V] += len(set(ds))

    ans = 0
    for k,i in cd.items():
        ans+=i
    return ans

def euler110():
    def calc_divs(exps):
        out = 1
        for e in exps:
            out = int(out)*int(2*e+1)
        return out
    
    def calc_n(ps,exps):
        out = 1
        for p,e in zip(ps,exps):
            tm = int(np.power(p,e))
            out = int(out)*int(tm)
        return out

    mn = 1.e25
    for nprimes in [8,9,10,11,12,13,14]:
        ps = utils.n_primes(nprimes)
        for e1 in range(1,10):
            exps = np.zeros(len(ps),dtype=int)
            exps[0] = e1
            mx = 0
            while True:
                mx += 1
                for e in range(2,len(exps)):
                    exps[e] = 1
                for e in range(1,len(exps)):
                    if exps[e] < exps[e-1] and exps[e] <= mx:
                        exps[e]+=1
                    if calc_divs(exps) > (8e6)-1:
                        n = calc_n(ps,exps)
                        if n < mn:
                            mn = copy.copy(n)
                if exps[1] >= exps[0]:
                    break

    return mn

if __name__ == '__main__':
    # ONE HUNDRED AND ONE:
    st = time.time()
    print(f'Problem 101: {euler101()} ({time.time()-st} s)')

    # ONE HUNDRED AND TWO:
    st = time.time()
    print(f'Problem 102: {euler102()} ({time.time()-st} s)')
    
    # ONE HUNDRED AND THREE:
    st = time.time()
    print(f'Problem 103: {euler103()} ({time.time()-st} s)')

    # ONE HUNDRED AND FOUR:
    st = time.time()
    print(f'Problem 104: {euler104()} ({time.time()-st} s)')

    # ONE HUNDRED AND FIVE:
    st = time.time()
    print(f'Problem 105: {euler105()} ({time.time()-st} s)')

    # ONE HUNDRED AND SIX (just over 1 minute):
    st = time.time()
    print(f'Problem 106: {euler106()} ({time.time()-st} s)')
    
    # ONE HUNDRED AND SEVEN:
    st = time.time()
    print(f'Problem 107: {euler107()} ({time.time()-st} s)')
    
    # ONE HUNDRED AND EIGHT:
    st = time.time()
    print(f'Problem 108: {euler108()} ({time.time()-st} s)')
    
    # ONE HUNDRED AND NINE:
    st = time.time()
    print(f'Problem 109: {euler109()} ({time.time()-st} s)')
    
    # ONE HUNDRED AND TEN:
    st = time.time()
    print(f'Problem 110: {euler110()} ({time.time()-st} s)')