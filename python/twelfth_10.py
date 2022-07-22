import numpy as np
import utils
import time
import copy

def euler111():
    return 'Not solved'

# This one is probably way longer than necessary...
# was going to do some clever stuff to optimise, but it's not that slow so whatever
def euler112(target=0.5):
    def add_one(n):
        ind = -1
        while True:
            if n[ind] != 9:
                n[ind]+=1
                break
            else:
                n[ind] = 0
                ind -= 1
        return n

    def calc_perc(b,n):
        N = ''
        for _ in n: N+=str(_)
        return b/float(N)

    n = [1,0,0]
    b = 0
    while calc_perc(b,n) < target:
        if all([_ == 9 for _ in n]):
            n = [1] + [0]*len(n)
        n = add_one(n)
        i = 0
        while True:
            if n[i] == n[i+1]:
                i+=1
                if i == len(n)-1: break
                continue
            sd = 'd' if n[i] > n[i+1] else 'u'
            break
        
        i+=1
        bounce = False
        while True:
            if i >= len(n)-1: break
            if n[i] == n[i+1]:
                i+=1 
                if i == len(n)-1: break
                continue
            nd = 'd' if n[i] > n[i+1] else 'u'
            if sd != nd:
                bounce = True
                break
            i+=1
        if bounce: b+=1
    ans = ''
    for _ in n: ans+=str(_)
    return int(ans)

if __name__ == '__main__':

    # ONE HUNDRED AND ELEVEN:
    st = time.time()
    print(f'Problem 111: {euler111()} ({time.time()-st} s)')

    # ONE HUNDRED AND TWELVE:
    st = time.time()
    print(f'Problem 112: {euler112(.99)} ({time.time()-st} s)')