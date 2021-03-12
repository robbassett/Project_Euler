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

if __name__ == '__main__':
    # NINTY ONE:
    st = time.time()
    print(f'Problem 91: {euler91(50)} ({time.time()-st} s)')
    
    # NINTY TWO:
    st = time.time()
    print(f'Problem 92: {euler92()} ({time.time()-st} s)')
