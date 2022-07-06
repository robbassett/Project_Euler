import numpy as np
import utils
import time
import copy
import matplotlib.pyplot as plt

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
 

if __name__ == '__main__':
    # ONE HUNDRED AND ONE:
    st = time.time()
    print(f'Problem 101: {euler101(10)} ({time.time()-st} s)')

    # ONE HUNDRED AND TWO:
    st = time.time()
    print(f'Problem 102: {euler102()} ({time.time()-st} s)')