import numpy as np
from utils import *
import matplotlib.pyplot as plt
import itertools
import time

# PROJECT EULER 31
def euler31(total):
    coins = [1,2,5,10,20,50,100,200]
    combs = np.zeros((total+1,len(coins)))
    for v in range(combs.shape[0]):
        target = v+1
        for i,c in enumerate(coins):
            if i == 0: combs[v][i] = 1
            elif c <= target:
                combs[v][i] = combs[v][i-1] + combs[target - c - 1][i]
            else:
                combs[v][i] = combs[v][i-1]
    return int(combs[-1][-1])

if __name__ == '__main__':
    # THIRTY ONE:
    st = time.time()
    print(f'Problem 31: {euler31(200)} ({time.time()-st} s)')
    
