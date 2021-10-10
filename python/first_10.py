import numpy as np
from utils import *

# PROJECT EULER 1
def natural_numbers_below(N):
    out = 0
    for i in range(1,N):
        if i%3 == 0 or i%5 == 0: out+=i
    return out

# PROJECT EULER 2
def even_fibo_sum(max_val):
    fibo = np.zeros(1)
    i = 3
    while fibo.max() < max_val:
        i+=1
        fibo = fibonacci(i)
    t = np.where(fibo%2 == 0)[0]
    return fibo[t].sum()

# PROJECT EULER 3
def largest_prime_factor(N):
    p = primes_lt_n(int(np.sqrt(N)))
    v = np.where(N%p == 0)[0]
    return p[int(v.max())]

# PROJECT EULER 4
def largest_palindrome(ndigit):
    
    def check_palindrome(v):
        if str(v)[::-1] == str(v):
            return True
        else:
            return False
        
    mxv = int('1'+ndigit*'0')-1
    if check_palindrome(mxv*mxv):
        return mxv*mxv
    
    st = mxv
    val = 0
    pal = False
    while pal == False:
        for i in range(st+1):
            if check_palindrome(st*(st-i)):
                tv = st*(st-i)
                break
        if tv > val: val = tv
        st-=1
        if st*st < val:
            pal = True
    return val

# PROJECT EULER 5:
def inclusive_divisor(N):
    vals = np.linspace(1,N,N)
    rems = np.ones(len(vals))
    ch = 0.
    while sum(rems) != 0:
        ch+=vals.max()
        rems = ch%vals
    return int(ch)

# PROJECT EULER 6:
def euler6(N):
    return int(np.sum(np.linspace(1,N,N))**2 - np.sum(np.linspace(1,N,N)**2.))

# PROJECT EULER 7:
def euler7(N):
    return n_primes(N)[-1]

# PROJECT EULER 8:
def euler8(ndig):
    def str_to_prod(s):
        return np.array([int(i) for i in s]).prod()
    
    N = 731671765313306249192251196744265747423553491949349698352031277450632623957831801698480186947885184385861560789112949495459501737958331952853208805511154069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    
    n = str(N)
    mx = 0
    for j in range(len(n)-ndig):
        t = n[j:j+ndig]
        if str_to_prod(t) > mx: mx = str_to_prod(t)

    return mx

# PROJECT EULER 9:
def euler9(target):

    a = 2
    done = False
    while not done:
        for b in range(1,a):
            c = np.sqrt(a*a + b*b)
            if int(c) == c:
                if a+b+c == target:
                    return np.array((a,b,int(c))).prod()
                    done = True
        if not done: a+=1

# PROJECT EULER 10:
def euler10(N):
    return np.sum(primes_lt_n(N))

if __name__ == '__main__':
    # ONE:
    print(f'Problem 1: {natural_numbers_below(1000)}')

    # TWO:
    print(f'Problem 2: {int(even_fibo_sum(4.e6))}')

    # THREE:
    print(f'Problem 3: {largest_prime_factor(600851475143)}')

    # FOUR:
    print(f'Problem 4: {largest_palindrome(3)}')

    # FIVE (SLOW!):
    print(f'Problem 5: {inclusive_divisor(20)}')

    # SIX:
    print(f'Problem 6: {euler6(100)}')

    # SEVEN:
    print(f'Problem 7: {euler7(10001)}')

    # EIGHT:
    print(f'Problem 8: {euler8(13)}')
    
    # NINE:
    print(f'Problem 9: {euler9(1000)}')

    # TEN:
    print(f'Problem 10: {euler10(2.e6)}')

    
