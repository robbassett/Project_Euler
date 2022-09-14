import numpy as np
import utils
import time
import copy

def euler124(mx=10,i=4):
    def rad(n):
        return utils.prod([_ for _ in utils.get_factors(n) if utils.is_prime(_)])

    x,y = [0]*mx,np.linspace(1,mx,mx).astype(int)
    for n in range(1,mx+1):
        x[n-1] = rad(n)
    
    t = np.argsort(x)
    return y[t[i-2]]

def euler125(d=3):
    st = 1
    ans = set([])
    while True:
        vs = [st*st]
        while True:
            vs.append((st+len(vs))*(st+len(vs)))
            x = sum(vs)
            if len(str(x)) > d:
                break

            if str(x) == str(x)[::-1]:
                ans.add(x)

        st += 1
        if len(str(st*st)) > d:
            break
    return sum(list(ans))

if __name__ == '__main__':

    # ONE HUNDRED AND TWENTY FOUR:
    st = time.time()
    print(f'Problem 124: {euler124(100000,10000)} ({time.time()-st} s)')
    
    # ONE HUNDRED AND TWENTY FIVE:
    st = time.time()
    print(f'Problem 125: {euler125(8)} ({time.time()-st} s)')