import numpy as np
from utils import *
import matplotlib.pyplot as plt
import itertools
import time

# PROJECT EULER 94
def euler94():
    def iso_area(s1,s2):
        h = np.sqrt(s1*s1 - (s2/2)*(s2/2))
        return 0.5*h*s2

    s1 = 1
    out = 0
    prev=1
    while True:
        s1 += 1
        if 2*s1 + (s1-1) > 1.e9:
            break
        if np.sqrt(3*s1*s1 + 2*s1 - 1)%1 == 0:
            out += int(2*s1) + int(s1 - 1)
            if s1 < 1000:
                s1*=3
            else:
                s1 = int(s1*3.73)
        elif np.sqrt(3*s1*s1 - 2*s1 -1)%1 == 0:
            out += int(2*s1) + int(s1 + 1)
            if s1 < 1000:
                s1*=3
            else:
                s1 = int(s1*3.73)

    return out

st = time.time()
print(euler94())
print(f'timed at {time.time()-st} s')


    
