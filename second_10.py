import numpy as np
from utils import *
import time

# PROJECT EULER 11:
def euler11():
    grid = '08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'

    grid = np.reshape(np.array(grid.split()).astype(float),(20,20))
    mx = 0
    for j in range(16):
        for i in range(20):
            try:
                tm = grid[i,j-4:j].prod()
                if tm > mx: mx = tm
            except:
                pass
            try:
                tm = np.array([grid[i+k,j-k] for k in range(4)]).prod()
                if tm > mx: mx = tm
            except:
                pass
            try:
                tm = grid[i,j:j+4].prod()
                if tm > mx: mx = tm
            except:
                pass
            try:
                tm = np.array([grid[i+k,j+k] for k in range(4)]).prod()
                if tm > mx: mx = tm
            except:
                pass
            try:
                tm = grid[i][j:j+4].prod()
                if tm > mx: mx = tm
            except:
                pass
    return int(mx)

# PROJECT EULER 12
def euler12(ndiv):
    done = False
    n=2
    while not done:
        tfcts = get_factors(np.linspace(1,n,n).sum())
        if len(tfcts) > ndiv:
            done = True
        else:
            n+=1
    return int(np.linspace(1,n,n).sum())

# PROJECT EULER 13
def euler13():
    d = np.loadtxt('aux/e13.dat',np.float64).sum()
    a = str(d)
    out = ''
    ind = 0
    while len(out) < 10:
        if a[ind] != '.': out+=a[ind]
        ind+=1
    return out

# PROJECT EULER 14
def euler14():
    def cseq(N):
        s = [N]
        n = N
        while n != 1:
            if n%2 == 0:
                n/=2
            else:
                n = 3*n + 1
            s.append(int(n))
        return s

    ls = []
    mx = int(1e6)
    a = 0
    v = 0
    for i in range(1,mx+1):
        seq = cseq(i)
        if len(seq) > a:
            a = len(seq)
            v = i

    return v

# PROJECT EULER 15
def euler15(N):
    prev = [1,2,3]
    row = 3
    while row <= N+1:
        new = [1 for i in range(row)]
        for i in range(1,row-1):
            new[i] = new[i-1]+prev[i]
        new[-1] = 2*new[-2]
        prev = [i for i in new]
        row += 1
    return new[-1]

# PROJECT EULER 16
def euler16(N):
    return np.sum([int(_) for _ in str(2**N)])

# PROJECT EULER 17
def euler17(N):
        
    count_dic = {
        1:3,
        2:3,
        3:5,
        4:4,
        5:4,
        6:3,
        7:5,
        8:5,
        9:4,
        10:3,
        11:6,
        12:6,
        13:8,
        14:8,
        15:7,
        16:7,
        17:9,
        18:8,
        19:8,
        20:6,
        30:6,
        40:5,
        50:5,
        60:5,
        70:7,
        80:6,
        90:6
    }

    count = 0
    for i in range(1,N+1):
        if len(str(i)) == 1:
            count += count_dic[i]
        elif len(str(i)) == 2:
            if i in count_dic.keys():
                count += count_dic[i]
            else:
                tens = int(str(i)[0]+'0')
                ones = int(str(i)[1])
                count += count_dic[tens]
                count += count_dic[ones]
        elif len(str(i)) == 3:
            count += count_dic[int(str(i)[0])]
            count += 7
            
            if i%100 != 0:
                tens = int(str(i)[1:])
                if tens in count_dic.keys():
                    count += count_dic[tens]
                else:
                    tt = int(str(tens)[0]+'0')
                    ones = int(str(tens)[1])
                    count += count_dic[tt]
                    count += count_dic[ones]
                count += 3
        else:
            count += len('onethousand')
    return count
                
if __name__ == '__main__':
    # ELEVEN
    st = time.time()
    print(f'Problem 11: {euler11()} ({time.time()-st} s)')
    
    # TWELVE
    st = time.time()
    print(f'Problem 12: {euler12(500)} ({time.time()-st} s)')

    # THIRTEEN
    st = time.time()
    print(f'Problem 13: {euler13()} ({time.time()-st} s)')

    # FOURTEEN
    st = time.time()
    print(f'Problem 14: {euler14()} ({time.time()-st} s)')

    # FIFTEEN
    st = time.time()
    print(f'Problem 15: {euler15(20)} ({time.time()-st} s)')

    # SIXTEEN
    st = time.time()
    print(f'Problem 16: {euler16(1000)} ({time.time()-st} s)')
    
    # SEVENTEEN
    st = time.time()
    print(f'Problem 17: {euler17(1000)} ({time.time()-st} s)')
