import numpy as np
import itertools
import copy

def char_position(letter):
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter.lower())-96

def get_pandigitals():
    pdn = list(itertools.permutations([1,2,3,4,5,6,7,8,9]))
    out = np.zeros(len(pdn)).astype(int)
    for i,p in enumerate(pdn):
        t = ''
        for v in p: t+=str(v)
        out[i] = int(t)
    return out

def factorial(N):
    if N != 0:
        return int(np.linspace(1,N,N).prod())
    else:
        return 1

def big_factorial(N):
    V = [1]
    carry = 0
    for n in np.linspace(2,N,N-1):
        for i,v in enumerate(V):
            carry,t = divmod(v*n + carry,10)
            V[i] = t
        if carry != 0:
            for c in str(int(carry))[::-1]:
                V = V+[int(c)]
            carry = 0
    return V
            

def fibonacci(Nterms):
    out = np.zeros(Nterms)
    out[0],out[1] = 1,2
    for i in range(Nterms-2):
        out[i+2] = out[i]+out[i+1]
    return out

def primes_lt_n(n):
    """ Returns  a list of primes < n """
    n = int(n)
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return np.array([2] + [2*i+1 for i in range(1,n//2) if sieve[i]])

def n_primes(n):
    """ Returns first n primes """
    p = [2]
    c = 2
    while len(p) < n:
        j = 0
        c += 1
        while j < len(p):
            if c % p[j] == 0:
                break
            elif j == len(p) - 1:
                p.append(c)
            j += 1
    return p

def is_prime(n):
    """function to find if the given
    number is prime"""
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def get_factors(n,excl_N=False):
    fcts = []
    for i in range(int(np.sqrt(n))):
        if n%(i+1) == 0:
            fcts.append(i+1)
            if (n/(i+1)) not in fcts:
                if (n/(i+1)) == n and excl_N:
                    pass
                else:
                    fcts.append(int(n/(i+1)))
    return fcts

def gcf(n1,n2):
    return max(set(get_factors(n1)).intersection(set(get_factors(n2))))

class sudoku():

    def __init__(self,gridlines):
        self.input = gridlines
        self.make_grid()
        self.possibles = {}
        self.check_set = set([0,1,2,3,4,5,6,7,8,9])
        self.unsolved = np.where(self.grid == 0)

    def to_terminal(self):
        print('-'*31)
        r = 0
        for row in self.grid:
            tr = '|'
            c = 0
            for v in row:
                c+=1
                if c == 4:
                    c=1
                    tr+='|'
                tr+=' '+str(int(v))+' '
            r+=1
            if r == 4:
                print('-'*31)
                r = 1
            tr += '|'
            print(tr)
        print('-'*31)

    def make_grid(self):
        self.grid = np.empty((9,9))
        for row,line in enumerate(self.input):
            line = line.replace('\n','')
            for col,val in enumerate(line):
                self.grid[row,col] = val

    def get_hidden_pairs(self,r,c):
        def check_relevant(kr,kc,r,c):
            if kr//3 == r//3 and kc//3 == c//3:
                return True
            if kr == r or kc == c:
                return True
            return False

        hidden = []
        tst = []
        for k,i in self.possibles.items():
            if f'{r},{c}' == k: continue
            kr,kc = int(k.split(',')[0]),int(k.split(',')[1])
            if check_relevant(kr,kc,r,c):
                for _k,_i in self.possibles.items():
                    if f'{r},{c}' == _k or k == _k or i != _i: continue
                    _kr,_kc = int(_k.split(',')[0]),int(_k.split(',')[1])
                    if check_relevant(_kr,_kc,kr,kc) and check_relevant(_kr,_kc,r,c):
                        hidden.append(i)
                        tst.append([kr,kc,_kr,_kc])

        return hidden,tst

    def get_cell_possibles(self,r,c):
        qr,qc = r//3,c//3
        sq = []
        for row in self.grid[3*qr:3*(qr+1)]:
            sq += list(row[3*qc:3*(qc+1)])
        sq = set(sq)
        row = set(self.grid[r])
        col = set(self.grid.T[c])

        excl = sq.union(row).union(col)

        return self.check_set.difference(excl)

    def init_check(self,r,c,incl_hidden=False):
        val = list(self.get_cell_possibles(r,c))
        if incl_hidden and len(val) == 3:
            hp,tst = self.get_hidden_pairs(r,c)
            for hidden,ttt in zip(hp,tst):
                tval = list(set(val).difference(set(hidden)))
                if len(tval) == 1:
                    self.grid[r,c] = tval[0]
                    if f'{r},{c}' in self.possibles.keys():
                        del self.possibles[f'{r},{c}']
                    return

        if len(val) == 1:
            self.grid[r,c] = val[0]
            if f'{r},{c}' in self.possibles.keys():
                del self.possibles[f'{r},{c}']
        else:
            if len(val) == 2:
                self.possibles[f'{r},{c}'] = val
            

    def solve_iter(self,hidden=False):
        for r,c in zip(*self.unsolved):
            self.init_check(r,c,incl_hidden=hidden)
        self.unsolved = np.where(self.grid == 0)
        
    def solve(self):
        while len(self.unsolved[0]) > 0:
            pgrid = self.grid.copy()
            self.solve_iter(hidden=True)
            ch = []
            for _ in (pgrid == self.grid): ch.append(all(_))
            if all(ch):
                break
        self.to_terminal()
            